from datetime import datetime
from pymongo import MongoClient

from utils import log
from config import MONGODB_CONNECTION_STRING

class Mongo:
    def __init__(self):
        self.client = MongoClient(MONGODB_CONNECTION_STRING)
        
        log("Connected to MongoDB")

        self.db = self.client.get_database("phalerum")
        self.agents = self.db.get_collection("agents")
        self.jobs = self.db.get_collection("jobs")
    
    def get_agent_amount(self):
        return self.agents.count_documents({})
    
    def get_job_amount(self):
        return self.jobs.count_documents({})