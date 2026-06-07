import csv
from kafka import KafkaProducer
import json
import time

# Підключення до Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092', 'localhost:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Читаємо CSV
with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Відправляємо в Topic1 і Topic2
        producer.send('Topic1', value=row)
        producer.send('Topic2', value=row)
        print(f"Sent: {row}")
        time.sleep(0.1)  # щоб не навантажувати брокер

producer.flush()
producer.close()