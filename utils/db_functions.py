from models.schemas import Measurement, Location
from sqlalchemy import desc
def store_measurement(session, temperature, humidity, co2, location_id):
    measurement = Measurement(temperature=temperature, 
                              humidity=humidity, 
                              co2=co2, 
                              location_id=location_id)
    session.add(measurement)
    session.commit()
    
def store_location(session, gps_location, location_name, location_description, username, password):
    new_location = Location(gps_location=gps_location, 
                            location_name=location_name, 
                            location_description=location_description, 
                            username=username, 
                            password=password)
    session.add(new_location)
    session.commit()
    
def get_measurements(session, interval):
    # Map interval to number of records to fetch
    interval_map = {
        '1h': 2,
        '12h': 24,
        '24h': 48,
        '1w': 336,  # 7 days * 48 records per day
        '1m': 1440  # 30 days * 48 records per day (assuming 30 days in a month)
    }

    if interval not in interval_map:
        raise ValueError("Invalid interval")

    num_records = interval_map[interval]

    # Fetch the last `num_records` measurements
    measurements = session.query(Measurement).order_by(desc(Measurement.timestamp)).limit(num_records).all()
    
    # Serialize the measurements
    measurements_data = [
        {
            'id': m.id,
            'temperature': m.temperature,
            'humidity': m.humidity,
            'co2': m.co2,
            'timestamp': m.timestamp,
            'location_id': m.location_id
        }
        for m in measurements
    ]
    
    return measurements_data