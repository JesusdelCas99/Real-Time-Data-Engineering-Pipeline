import requests
from kafka import KafkaProducer
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def getUserInfoAndSendToKafka():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()

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
    producer = KafkaProducer(bootstrap_servers='172.20.10.3:9092')
    producer.send('userInfoTopic', json.dumps(userInfo).encode('utf-8'))
    producer.flush()
    producer.close()


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=0),
}

dag = DAG(
    'get_user_info_and_send_to_kafka',
    default_args=default_args,
    description='Fetch user info from randomuser.me and send to Kafka',
    schedule_interval=timedelta(seconds=30),  # Runs every 30 seconds
)

getUserInfoAndSendToKafka_task = PythonOperator(
    task_id='get_user_info_and_send_to_kafka',
    python_callable=getUserInfoAndSendToKafka,
    dag=dag,
)


    

