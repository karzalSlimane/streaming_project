# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables for Kafka, Spark, MongoDB, Cassandra
ENV KAFKA_VERSION=2.8.0
ENV SPARK_VERSION=3.1.1
ENV CASSANDRA_VERSION=3.11
ENV MONGO_VERSION=4.2

# Install Java, wget, curl and other dependencies
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget curl bash && \
    apt-get clean

# Install Python libraries
RUN pip install kafka-python pyspark pymongo cassandra-driver streamlit

# Set working directory
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Expose the necessary ports
EXPOSE 9093 27017 9042 7077 8888

# Command to start your app (could be adjusted depending on your entry point)
CMD ["python3", "src/producer/data_producer.py"]
