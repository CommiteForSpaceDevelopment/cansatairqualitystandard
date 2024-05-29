from models.schemas import Measurement, Location

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