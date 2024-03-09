-- Create the keyspace if it doesn't exist
CREATE KEYSPACE IF NOT EXISTS spark_stream WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS spark_stream.userinfo (
    id UUID PRIMARY KEY,
    username TEXT,
    password TEXT,
    name TEXT,
    phone TEXT,
    email TEXT,
    city TEXT,
    state TEXT,
    country TEXT
);

