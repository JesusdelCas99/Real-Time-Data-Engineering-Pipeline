# Real time Data Engineering Pipeline with Apache Airflow, Apache Kafka, Apache Spark, Cassandra and PostgreSQL

This repository provides a detailed guide for constructing a robust end-to-end data engineering pipeline that covers each stage from data ingestion to processing and finally to storage. The pipeline is orchestrated using Apache Airflow and encapsulated within Docker containers for scalability and efficient management. 

  1. **Data Extraction**: Utilizing the https://randomuser.me/api/ API to retrieve user data at 30-second intervals.
  2. **Data Storage**: Storing the extracted data as a Kafka topic for seamless streaming.
  3. **Real-Time Processing**: Employing a Spark Cluster consumer group for real-time data processing.
  4. **Data Storage**: Persisting the processed data in a Cassandra database for further analysis and retrieval.

This project leverages a robust tech stack for seamless data handling that includes:

- **Apache Airflow**: A platform for programmatically authoring, scheduling, and monitoring workflows.
- **PostgreSQL**: An open-source relational database management system known for its reliability and robustness.
- **Apache Spark**: A fast and general-purpose cluster computing system for big data processing.
- **Cassandra**: A distributed NoSQL database designed for high scalability and fault tolerance.
- **Apache Kafka** (with KRaft): A distributed streaming platform used for building real-time data pipelines and streaming applications.
- **Control Center**: A comprehensive management and monitoring tool for Apache Kafka clusters, providing insights into cluster health, performance, and security.
- **Schema Registry**: A centralized repository for managing Avro schemas used in Kafka topics, ensuring data compatibility and consistency across different services.
- **Docker**: A platform for developing, shipping, and running applications in containers for ease of deployment and scalability.

## Usage

http://127.0.0.1:9021: Control Center for Kafka
http://127.0.0.1:9090: Web Server for Spark Cluster
http://127.0.0.1:8081: Web Server for Airflow

1. Levantamos la arquitectura de microservicios usando docker-compose up
2. Accedemos a la interfaz web de Airflow y activamos el elemento de DAG
3. Accedemos a la interfaz web del cluster de kafka para ver que efectivamente se esta enviando informacion de la API
4. Para verificar que todo funciona correctamente, accede a la terminal del contenedor de cassandra y ejecuta el siguiente comando: cqlsh -u cassandra -p cassandra 172.20.10.10 9042 -e "SELECT * FROM spark_stream.userinfo;"

## Directory Structure

Project files and folder structure:

- `airflow/`: Contains Apache Airflow DAGs and logs.
- `cassandra/`: Contains initialization scripts for Cassandra.
- `spark/`: Contains Spark streaming script and logs.
- `.env/`: Contains environment configuration files.
- `docker-compose.yml`: Docker Compose configuration file.
    
#### Environment Configuration

The repository includes several `.env` files that contain environment variables necessary for configuring different services. Below is a brief overview of each `.env` file:

- `.env/airflow.env`: Contains environment variables for configuring Apache Airflow.
- `.env/cassandra.env`: Contains environment variables for configuring Cassandra.
- `.env/control-center.env`: Contains environment variables for configuring Confluent Control Center.
- `.env/kafka.env`: Contains environment variables for configuring Apache Kafka.
- `.env/postgres.env`: Contains environment variables for configuring PostgreSQL.
- `.env/schema-registry.env`: Contains environment variables for configuring Schema Registry.
- `.env/spark-worker.env`: Contains environment variables for configuring Apache Spark.

## Acknowledgments

For detailed information about the code and its functionalities, please refer to the inline comments within the source files. Feel free to explore the codebase and contribute to further enhancements or bug fixes!
