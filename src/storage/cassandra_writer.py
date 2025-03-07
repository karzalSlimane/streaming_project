from cassandra.cluster import Cluster

# Cassandra client setup
cluster = Cluster(['cassandra'])
session = cluster.connect('user_data')

def store_in_cassandra(location, avg_age):
    session.execute("""
        INSERT INTO aggregates (location, avg_age)
        VALUES (%s, %s)
    """, (location, avg_age))
    print(f"Stored in Cassandra: {location}, {avg_age}")
