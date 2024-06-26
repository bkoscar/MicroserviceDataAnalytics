import random
import pandas as pd
from datetime import datetime, timedelta
NUM_DATA_POINTS_AND_DELTA_MINUTES = 50

class SensorData:
    def __init__(self, timestamp, temperature, humidity, pressure, wind_speed, wind_direction, co2_levels, luminosity, failure):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.co2_levels = co2_levels
        self.luminosity = luminosity
        self.failure = failure

    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": self.pressure,
            "wind_speed": self.wind_speed,
            "wind_direction": self.wind_direction,
            "co2_levels": self.co2_levels,
            "luminosity": self.luminosity,
            "failure": self.failure
        }


class DataGenerator:
    @staticmethod
    def generate_temperature():
        return round(random.uniform(15.0, 25.0), 2)

    @staticmethod
    def generate_humidity():
        return round(random.uniform(30.0, 70.0), 2)

    @staticmethod
    def generate_pressure():
        return round(random.uniform(980.0, 1050.0), 2)

    @staticmethod
    def generate_wind_speed():
        return round(random.uniform(0.0, 15.0), 2)

    @staticmethod
    def generate_wind_direction():
        return random.randint(0, 360)

    @staticmethod
    def generate_co2_levels():
        return round(random.uniform(300.0, 500.0), 2)

    @staticmethod
    def generate_luminosity():
        return round(random.uniform(100.0, 10000.0), 2)

    @staticmethod
    def generate_failure(temperature, humidity, pressure, wind_speed, wind_direction, co2_levels, luminosity):
        if temperature < 16 or temperature > 24:
            return 1
        if humidity < 35 or humidity > 65:
            return 1
        if pressure < 985 or pressure > 1045:
            return 1
        if wind_speed < 1 or wind_speed > 14:
            return 1
        if co2_levels < 310 or co2_levels > 490:
            return 1
        if luminosity < 200 or luminosity > 9500:
            return 1
        return 0

    @staticmethod
    def generate_data_points():
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=NUM_DATA_POINTS_AND_DELTA_MINUTES)
        data_points = []
        current_time = start_time
        for _ in range(NUM_DATA_POINTS_AND_DELTA_MINUTES):
            temperature = DataGenerator.generate_temperature()
            humidity = DataGenerator.generate_humidity()
            pressure = DataGenerator.generate_pressure()
            wind_speed = DataGenerator.generate_wind_speed()
            wind_direction = DataGenerator.generate_wind_direction()
            co2_levels = DataGenerator.generate_co2_levels()
            luminosity = DataGenerator.generate_luminosity()
            failure = DataGenerator.generate_failure(temperature, humidity, pressure, wind_speed, wind_direction, co2_levels, luminosity)
            data_point = SensorData(current_time, temperature, humidity, pressure, wind_speed, wind_direction, co2_levels, luminosity, failure)
            data_points.append(data_point.to_dict())
            current_time += timedelta(minutes=1)
        return data_points

