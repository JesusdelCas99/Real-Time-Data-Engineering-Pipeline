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



![Nombre Opcional](/images/system_architecture.png)

## Table of Contents

- [Usage](#usage)
- [Repository Structure](#repository-structure)
- [Environment Configuration](#environment-configuration)
- [Acknowledgments](#acknowledgments)

## Usage

Before running this project, make sure you have Docker and Docker Compose installed on your machine. Once installed, follow these step-by-step instructions:

  1. Clone the repository to your local machine: 
       ```
      git clone https://github.com/JesusdelCas99/Real-Time-Data-Engineering-Pipeline.git
      ```
  2. Launch Docker Desktop and execute the Docker Compose project configuration file:
      ```
      docker-compose up
      ```
  3. Access the Apache Airflow web interface at http://user:admin@127.0.0.1:2040.
  4. Once logged in, activate DAG `get_user_info_and_send_to_kafka`.
  7. Access Kafka Control Center cluster web interface at http://127.0.0.1:9021 and verify that user information is being sent from the API to the *userInfoTopic*.
  8. (Optional) Access the Apache Spark Cluster web interface at http://127.0.0.1:9090 to view detailed information about cluster health and worker resources.
  9. Open Docker Desktop, navigate to the terminal window of the `cassandra` container and execute the following command:

     ```
     cqlsh -u cassandra -p cassandra 172.20.10.10 9042 -e "SELECT * FROM spark_stream.userinfo;"
     ```
      The preceding command should yield a response akin to the following. Upon each execution of the command, fresh records will be appended to the userinfo table, as they are streamed in real-time from the API.
      ```
      # cqlsh -u cassandra -p cassandra 172.20.10.10 9042 -e "SELECT * FROM spark_stream.userinfo;"
      
          id                                  | city          | country     | email                               | name      | password  | phone          | state                        | username
        --------------------------------------+---------------+-------------+-------------------------------------+-----------+-----------+----------------+------------------------------+----------------------
         da27f8c2-3aa2-4015-8037-30686638ae42 |       Limeira |      Brazil |          fausta.peixoto@example.com |    Fausta |  rsalinas | (11) 2928-9052 |                        Ceará |      brownostrich595
         6a0cf79c-186a-465b-a2e0-a785513674db | Coffs Harbour |   Australia |              alice.reed@example.com |     Alice |   frances |   07-5498-1948 | Australian Capital Territory |         tinytiger379
         7de8a747-bfa3-4639-9b63-f193dee3c8d0 |         Field |      Canada |            lily.lavigne@example.com |      Lily |    getoff |   R62 T34-5668 |        Northwest Territories |        goldenduck868
         ec08a2e4-7816-4b6d-bf8a-e54cc64f8d67 |      Donabate |     Ireland |         gerald.stephens@example.com |    Gerald |    karina |   011-345-1178 |                        Louth |         tinyzebra989
         4063df64-1c92-4ec2-96ce-65fa88a63305 |        Oppdal |      Norway |        hamza.gerhardsen@example.com |     Hamza |   abgrtyu |       79457808 |               Nord-Trøndelag | ticklishbutterfly431
         f1ec4252-6a17-44bb-922a-070a59795e26 |    Alcobendas |       Spain |           sofia.vazquez@example.com |     Sofia |   tickler |    923-094-300 |           Castilla la Mancha |         greenbear310
      ```

## Repository Structure

Project files and folder structure:

- `airflow/`: Contains Apache Airflow DAGs and logs.
- `cassandra/`: Contains initialization scripts for Cassandra.
- `spark/`: Contains Spark streaming script and logs.
- `.env/`: Contains environment configuration files.
- `docker-compose.yml`: Docker Compose configuration file.

## Acknowledgments

For detailed information about the code and its functionalities, please refer to the inline comments within the source files. Feel free to explore the codebase and contribute to further enhancements or bug fixes!
