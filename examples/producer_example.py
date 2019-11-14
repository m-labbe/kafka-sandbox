from confluent_kafka import Producer
from datetime import datetime, timedelta
from dateutil import tz
from math import fmod
from typing import Tuple

location_mapped_to_temp_in_ranges = {
    "Pittsburgh-PA-US": range(65, 95),
    "San Francisco-CA-US": range(50, 80),
    "Sydney-NSW-AU": range(45, 75),
    "Mumbai-NH-IN": range(70, 100),
    "London-UK-GB": range(45, 75)
}
location_hour_offset = [0, -3, 14, 9, 6]
weather_types = ["Sunny", "Cloudy", "Fog", "Rain", "Lightning", "Windy"]
humidities = range(30, 100)
wind_speed_mph = range(0, 20)

ET = tz.gettz("America/New_York")
starting_datetime = datetime(2018, 6, 1, 0, 0, 0, 0, tzinfo=ET)

# Create Kafka Producer
# https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.Producer.Producer
# https://docs.confluent.io/current/installation/configuration/producer-configs.html
producer = Producer({"bootstrap.servers": "localhost:9092"})

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {0}: {1}")
    else:
        print(f"Message produced: {0}")

def generate_weather_strings(current_generation: int, current_datetime: datetime) -> Tuple[str, str]:
    for index, (location, temps) in enumerate(location_mapped_to_temp_in_ranges.items()):
        current_day = current_generation / 24
        base_current_hour = fmod(current_generation + location_hour_offset[index], 24) 
        current_temp_index = ((12 - (base_current_hour % 12) if (base_current_hour > 12)  else base_current_hour) + current_day) % len(temps)
        temp = temps[int(current_temp_index)]
        weather = weather_types[int((current_day + index) % len(weather_types))]
        humidity = int((current_day + base_current_hour + index) % len(humidities))
        windspeed = wind_speed_mph[int((current_day + (base_current_hour / 12) + index) % len(wind_speed_mph))]
        yield (location, f"{current_datetime},{temp},{weather},{humidity},{windspeed}")


try:
    print(">>> Press [Ctrl-C] to stop the producer")
    topic = "weather"
    current_generation = 0
    current_datetime = starting_datetime
    while True:
        for location, weather_string in generate_weather_strings(current_generation, current_datetime):
            print(f"{location}: {weather_string}")
            # produce message to topic asynchronously, providing the acked callback
            # https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.Producer.produce
            producer.produce(topic, value=weather_string, callback=acked)
            producer.poll(0.5)
            current_generation = current_generation + 1
            current_datetime = current_datetime + timedelta(hours=1)
except KeyboardInterrupt:
    print(">>> Producer stopped")
    pass

# Flush waits for all messages in Producer queue to be delivered, can assign a callback
# https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.Producer.flush
producer.flush(1)

