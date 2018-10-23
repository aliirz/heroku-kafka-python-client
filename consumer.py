
from kafka_helper import *
from kafka import KafkaConsumer, KafkaProducer


# Before creating Kafka Consumer, Please make sure that you have following
# environment variables set
# - KAFKA_URL
# - KAFKA_CLIENT_CERT
# - KAFKA_CLIENT_CERT_KEY
# - KAFKA_PREFIX
# - KAFKA_TRUSTED_CERT


consumer = KafkaConsumer(
    "your_topic",
    bootstrap_servers=get_kafka_brokers(),
    security_protocol='SSL',
    ssl_context=get_kafka_ssl_context(),
    auto_offset_reset='earliest', enable_auto_commit=False
)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print message
