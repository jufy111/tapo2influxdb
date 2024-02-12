# config.py

# Define your sensors here, IP and a name, add as many as you want
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
    'sample_time': 10,
    'timeout_time': 1 #timeout for query in seconds
}
