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
- **Apache Kafka** (with KRaft): A distributed streaming platform used for building real-time streaming applications.
- **Control Center**: A comprehensive management and monitoring tool for Apache Kafka clusters.
- **Schema Registry**: A centralized repository for managing Avro schemas used in Kafka topics.
- **Docker**: A platform for developing, shipping, and running applications in containers for ease of deployment.

## Prerequisites

Before running this project, make sure you have Docker and Docker Compose installed on your machine.
    
## Usage

  
  1. Open Docker Desktop and launch the Docker Compose project configuration file:

    ```
    docker-compose up
    ```
     
  3. Access Airflow web interface at http://127.0.0.1:8081. Log in using the following credentials: <*Username*=user>, <*Password*=admin>.
  4. Once logged in, activate DAG `get_user_info_and_send_to_kafka`.
  5. Access Kafka Control Center cluster web interface at http://127.0.0.1:9021 and verify that user information is being sent from the API to the *userInfoTopic*.
  6. (Optional) Access the Apache Spark Cluster web interface at http://127.0.0.1:9090 to view detailed information about cluster health and worker resources.
  7. Open Docker Desktop and navigate to spark-submmit container "terminal" window. There write the following command to verify everything is working:

     ```
     cqlsh -u cassandra -p cassandra 172.20.10.10 9042 -e "SELECT * FROM spark_stream.userinfo;"
     ```

  if things are working properly, the below command should give you a response like the following, were each time you write it again, new registries are being add to the
  the overall userinfo table:

  ```
  id                                   | city          | country     | email                               | name      | password  | phone          | state                        | username
--------------------------------------+---------------+-------------+-------------------------------------+-----------+-----------+----------------+------------------------------+----------------------
 7fa1d4c1-fa7e-4b7f-b967-794b0f9ff7e6 |        بروجرد |        Iran |               mrl.hsyny@example.com |     مارال |  mortgage |   022-96041359 |               آذربایجان شرقی |       organicfish264
 951a803c-21c8-4798-aa65-67ee119363b1 |     Järvenpää |     Finland |              toivo.palo@example.com |     Toivo |    elway7 |     08-115-376 |                      Uusimaa |    beautifulsnake682
 dc3c2b7f-57b2-4586-b125-ba6d1f8d255f | Kahramanmaraş |      Turkey |             murat.ozbir@example.com |     Murat |     spoon | (844)-413-9472 |                      Erzurum |         heavyswan844
 68b90e7b-89a4-4afe-9b80-3efb84876a27 |      Cornwall |      Canada |              felix.park@example.com |     Felix |     rebel |   P17 K15-7562 |                      Alberta |         brownbird784
 f085b20e-43f4-4ef8-aa43-613ad8bb16c5 |        Løstad |      Norway |         adrian.mohammad@example.com |    Adrian |  dolemite |       68782109 |                     Rogaland |      organicpanda534
  ```


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
