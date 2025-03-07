import streamlit as st
import pandas as pd
from kafka import KafkaConsumer
import json

# Kafka consumer to fetch real-time data
consumer = KafkaConsumer(
    'user-data',
    bootstrap_servers=['kafka:9093'],
    auto_offset_reset='earliest',
    group_id='dashboard-group'
)

st.title('Real-Time User Data Dashboard')

# Fetch messages from Kafka and display
for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    df = pd.DataFrame([data])

    st.write(df)
