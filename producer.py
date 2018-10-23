import kafka_helper


# Before creating Kafka Consumer, Please make sure that you have following
# environment variables set
# - KAFKA_URL
# - KAFKA_CLIENT_CERT
# - KAFKA_CLIENT_CERT_KEY
# - KAFKA_PREFIX
# - KAFKA_TRUSTED_CERT


producer = kafka_helper.get_kafka_producer()
resp = producer.send('your_topic', key='SomeKey', value={'Name': 'Hassan'})
print resp.__dict__
