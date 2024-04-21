from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

from utils import log
from config import INFLUXDB_TOKEN, INFLUXDB_ORG, INFLUXDB_URL, INFLUXDB_BUCKET

class Influx:
    def __init__(self):
        self.client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
        log("Connected to InfluxDB")

    def write(self, measurement, field, value):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        point = Point(measurement).field(field, value)
        write_api.write(bucket=INFLUXDB_BUCKET, record=point)