import requests
from kafka import KafkaProducer
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


# Function to fetch user info from randomuser.me and send it to Kafka
def getUserInfoAndSendToKafka():
    # Fetch user info from randomuser.me API
    response = requests.get("https://randomuser.me/api/")
    data = response.json()

    # Extract required user info from API response
    userInfo = {
        'username': data['results'][0]['login']['username'],
        'password': data['results'][0]['login']['password'],
        'name': data['results'][0]['name']['first'],
        'phone': data['results'][0]['phone'],
        'email': data['results'][0]['email'],
        'city': data['results'][0]['location']['city'],
        'state': data['results'][0]['location']['state'],
        'country': data['results'][0]['location']['country']
    }

    # Send userInfo to Kafka
    producer = KafkaProducer(bootstrap_servers='172.20.10.3:9092')  # Kafka producer instance
    producer.send('userInfoTopic', json.dumps(userInfo).encode('utf-8'))  # Send user info to Kafka topic
    producer.flush()  # Flush the producer to ensure all messages are sent
    producer.close()  # Close the producer connection


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',  # Owner of the DAG
    'depends_on_past': False,  # Whether the DAG depends on past runs
    'start_date': datetime(2024, 3, 7),  # Start date of the DAG
    'email_on_failure': False,  # Whether to send email on failure
    'email_on_retry': False,  # Whether to send email on retry
    'retries': 0,  # Number of retries
    'retry_delay': timedelta(seconds=0),  # Delay between retries
}

# Define the DAG
dag = DAG(
    'get_user_info_and_send_to_kafka',  # Dag name
    default_args=default_args,  # Default arguments
    description='Fetch user info from randomuser.me and send to Kafka',  # DAG description
    schedule_interval=timedelta(seconds=30),  # Runs every 30 seconds
)

# Define the task to execute the getUserInfoAndSendToKafka function
getUserInfoAndSendToKafka_task = PythonOperator(
    task_id='get_user_info_and_send_to_kafka',  # Task ID
    python_callable=getUserInfoAndSendToKafka,  # Function to execute
    dag=dag,  # Associated DAG
)


    

