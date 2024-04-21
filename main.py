import sys
from time import sleep

from utils import log
from utils import getCurrentMinute
from mongo import Mongo
from influx import Influx

class Recorder():
    def __init__(self):
        self.mongo = Mongo()
        self.influx = Influx()

    def start(self):
        log("Starting recorder")
        try:
            while True:
                if (getCurrentMinute() == "00"):
                    log("Recording data")
                    agent_amount = self.mongo.get_agent_amount()
                    job_amount = self.mongo.get_job_amount()
                    self.influx.write("agents", "amount", agent_amount)
                    self.influx.write("jobs", "amount", job_amount)
                    sleep(60)
        except KeyboardInterrupt:
            log("Stopping recorder")
            sys.exit(0)
    

if __name__ == "__main__":
    recorder = Recorder()
    recorder.start()