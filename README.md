# IIIF Format Presentation API Server

## Pre-requisites

1. Docker is installed
2. Optionally, Python 3.9 or higher is installed
3. An IIIF Image API V3 server is running

## Docker-based Instructions (Recommended)

### Build the image

```bash
docker build -t iiif-presentation-api-server .
```

### Run the container

```bash
# This assumes that an IIIF Image API V3 server is running on the host machine at port 8182
docker run -p 8002:8000 --env IIIF_IMAGE_API_SERVER_URL=http://host.docker.internal:8182/iiif/3 iiif-presentation-api-server
```

## API Documentation

After starting the server, the API documentation will be available at `http://localhost:8002/docs`.

## Usage

### Get manifest for a given image

This assumes that a file with name `CATS_MM14_C_F1_XPL-big.tif` is available in the IIIF Image API server.

```bash
curl -X 'GET' \
  'http://localhost:8002/api/v1/manifests/CATS_MM14_C_F1_XPL-big.tif/manifest.json' \
  -H 'accept: application/json'
```

### Health check

```bash
curl -X 'GET' \
  'http://localhost:8002/api/v1/ok' \
  -H 'accept: application/json'
```

## Local Installation Instructions (Alternative)

### Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Run the server

```bash
export PYTHONPATH=$PWD/app
python -m uvicorn app.main:app --reload --port 8002
```
