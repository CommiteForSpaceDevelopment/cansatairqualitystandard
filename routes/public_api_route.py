from flask import Blueprint, request, jsonify
from utils.db_functions import store_measurement, store_location
from config.app_config import web_app
from utils.db_service import init_db, init_db_and_create_tables


@web_app.route('/api/send_measurement', methods=['POST'])
def send_measurement():
    data = request.json

    # Extract required fields from the JSON payload
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    co2 = data.get('co2')
    location_id = data.get('location_id')

    # Check if all required fields are present
    if None in (temperature, humidity, co2, location_id):
        return jsonify({'error': 'Missing required fields'}), 400
    session = init_db()
    # Store the measurement in the database
    store_measurement(session, temperature=temperature, humidity=humidity, co2=co2, location_id=location_id)

    return jsonify({'message': 'Measurement received successfully'}), 200

@web_app.route('/api/store_location', methods=['POST'])
def store_location_route():
    data = request.json
    
    # Extract data from JSON request
    gps_location = data.get('gps_location')
    location_name = data.get('location_name')
    location_description = data.get('location_description')
    username = data.get('username')
    password = data.get('password')
    session = init_db()
    try:
        store_location(session=session,
                       gps_location=gps_location, 
                       location_name=location_name, 
                       location_description=location_description, 
                       username=username, 
                       password=password)
        return jsonify({'message': 'Location stored successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500