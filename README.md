# Recorder

Recorder retrieves data from MongoDB every hour and pushes it to InfluxDB.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. The project uses the following Python packages:

- influxdb_client
- pymongo[srv]

You can install them using pip:

```sh
pip install -r requirements.txt
```

### Configuration
The project requires a configuration file config.py with the following variables:

- `MONGODB_CONNECTION_STRING`: Connection string for MongoDB, should be in the format "mongodb://:@:/"
- `INFLUXDB_TOKEN`: Token for InfluxDB, should be in base64 format
- `INFLUXDB_ORG`: Name of the organization in InfluxDB
- `INFLUXDB_URL`: URL of the InfluxDB instance
- `INFLUXDB_BUCKET`: Name of the bucket in InfluxDB

### Running the Project
You can run the project using the following command:

```sh
python3 main.py
```

### Docker
The project also includes a `Dockerfile` for building a Docker image of the project. You can build the image using the following command:

```sh
docker build -t recorder .
```

and run with:

```sh
docker run -it --rm --name my-running-app my-python-app
```