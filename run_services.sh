#!/bin/bash

# Navigate to the docker directory where the docker-compose.yml is located
cd docker

# Step 1: Build Docker images
echo "Building Docker images..."
docker compose build

# Step 2: Start Docker containers in detached mode
echo "Starting Docker containers..."
docker compose up -d

# Step 3: Wait for the services to be fully up and running
echo "Waiting for services to initialize..."
sleep 20  # Adjust the sleep time if needed, depending on the service startup time.

# Step 4: Run Kafka Producer to simulate data
echo "Running Kafka Producer..."
docker compose exec -T python python3 src/producer/data_producer.py &

# Step 5: Run PySpark Structured Streaming
echo "Running PySpark Structured Streaming..."
docker compose exec -T pyspark python3 src/streaming/stream_processing.py &

# Step 6: Run MongoDB Writer to insert raw data
echo "Running MongoDB Writer..."
docker compose exec -T python python3 src/mongo_writer.py &

# Step 7: Run Cassandra Writer to insert aggregated data
echo "Running Cassandra Writer..."
docker compose exec -T python python3 src/cassandra_writer.py &

# Step 8: Run Streamlit Dashboard
echo "Starting Streamlit Dashboard..."
docker compose exec -T streamlit streamlit run src/app.py &

# Step 9: Run unit tests automatically
echo "Running tests..."
docker compose exec -T python pytest > result.log; tail -n 20 result.log  # Show the last 20 lines of the result

# Step 10: Monitor logs for all services (optional)
echo "Monitoring logs (press Ctrl+C to stop)..."
docker compose logs -f

# Step 11: Clean up (optional)
# echo "Stopping and cleaning up services..."
#docker compose down
