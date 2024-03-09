#!/bin/bash

# Set the IP address and port for the Cassandra server
host="172.20.10.10"
port="9042"

# Wait for the Cassandra server to become available
while ! cqlsh "$host" "$port" -u cassandra -p cassandra --connect-timeout=5 -e "SHOW VERSION;" > /dev/null 2>&1; do
  # If the server is not available, print an error message and sleep for 5 seconds before retrying
  echo "Cassandra is unreachable at $host:$port - sleeping for 5 seconds"
  sleep 5
done

# Once the server is available, print a success message
echo "Cassandra is up and running at $host:$port"

# Create initial keyspace for the application
echo "Creating initial keyspace for application..."
cqlsh -u cassandra -p cassandra 172.20.10.10 9042 -f /tmp/cassandra-init.cql
echo "Keyspace successfully created!"

# Infinite loop to keep the service running and accept new connections
echo "Service is up and running!"
while true; do
  :
done