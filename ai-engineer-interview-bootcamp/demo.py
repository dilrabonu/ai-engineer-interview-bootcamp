"""You have two CSV files:

temperature_data.csv – Contains temperature readings from sensors.
device_status.csv – Contains device status (e.g., ON/OFF) over time.
Each file includes timestamps, but the readings are not always aligned. Your job is to:

Join both datasets using a time-based merge (asof merge).
Forward-fill missing status values.
Filter for records where the device was ON.
Calculate the average temperature per hour when the device was ON.
"""



import pandas as pd

# Step 1: Create the temperature DataFrame

temperature_data = {

    'timestamp': [

        '2025-10-23 08:00:00', '2025-10-23 08:05:00', '2025-10-23 08:10:00',

        '2025-10-23 08:20:00', '2025-10-23 08:35:00', '2025-10-23 08:50:00',

        '2025-10-23 09:00:00', '2025-10-23 09:10:00'

    ],

    'temperature': [22.1, 22.3, 22.5, 22.6, 22.8, 23.0, 23.3, 23.5]

}

df_temp = pd.DataFrame(temperature_data)

df_temp['timestamp'] = pd.to_datetime(df_temp['timestamp'])

df_temp = df_temp.sort_values('timestamp')

# Step 2: Create the device status DataFrame

status_data = {

    'timestamp': [

        '2025-10-23 08:00:00', '2025-10-23 08:15:00',

        '2025-10-23 08:45:00', '2025-10-23 09:05:00'

    ],

    'status': ['OFF', 'ON', 'OFF', 'ON']

}

df_status = pd.DataFrame(status_data)

df_status['timestamp'] = pd.to_datetime(df_status['timestamp'])

df_status = df_status.sort_values('timestamp')