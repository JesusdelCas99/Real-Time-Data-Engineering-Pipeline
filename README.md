# Real-time-Data-Pipeline-with-Airflow-Kafka-Spark-Cassandra

http://127.0.0.1:9021: Control Center for Kafka
http://127.0.0.1:9090: Web Server for Spark Cluster
http://127.0.0.1:8081: Web Server for Airflow

1. Levantamos la arquitectura de microservicios usando docker-compose up
2. Accedemos a la interfaz web de Airflow y activamos el elemento de DAG
3. Accedemos a la interfaz web del cluster de kafka para ver que efectivamente se esta enviando informacion de la API
4. Para verificar que todo funciona correctamente, accede a la terminal del contenedor de cassandra y ejecuta el siguiente comando: cqlsh -u cassandra -p cassandra 172.20.10.10 9042 -e "SELECT * FROM spark_stream.userinfo;"
