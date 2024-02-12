Smart Plug Data Collection and InfluxDB Integration

This Python script collects real-time data from TP-Link smart plugs and pushes it to an InfluxDB instance for storage and analysis. It interfaces with TP-Link devices using a custom query mechanism, decrypts the returned data, and formats it to be compatible with InfluxDB's write protocol. This project is particularly useful for monitoring power consumption and energy usage of various devices.

 ### Python dependencies
  pip install PyP100  
  pip install influxdb_client    
  
Huge shoutout to fishbloger for the PyP100 library  
https://github.com/fishbigger/TapoP100

Usage

    Clone the repository.
    Modify the configuration variables in the config.py file to match your setup.
    Run the tapo2influxdb.py script to start data collection and InfluxDB integration.
    Collected data will be stored in your InfluxDB instance for further analysis.

Note: This repository provides a foundational structure for integrating Tapo TP-Link smart plug data with InfluxDB. Feel free to customize and expand the project according to your requirements.

# config.py
```
# Sensor Definition
sensor_data = [
    {'ip': '10.10.10.101', 'name': 'devicename1'},
    {'ip': '10.10.10.102', 'name': 'devicename2'},
    {'ip': '10.10.10.103', 'name': 'devicename3'}
    # ... add other sensors ...
]

# InfluxDB Configuration
influxdb_config = {
    'token': "yourtokenhere",
    'org': "yourorg",
    'bucket': "bucketnamehere",
    'dburl': "http://10.10.10.10:8086"  #IP and port of you influxdb instance
}

# TP link Tapo Config
tapo_config = {
    'username':'YourTapoLogin@email.com',
    'password':'YourTapoPassword'
}

# Other Configuration
other_config = {
    'port': 9999,  #this is the port the kasa devices use, leave as is.
    'sample_time': 10,
    'timeout_time': 1 #timeout for query in seconds
}
```
