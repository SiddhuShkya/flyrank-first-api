# First API Endpoint

This is my first assignment for FlyRankAI internship, where I have to built a small api using Python & Flask.

## Endpoints

- `/` - Returns a JSON response with the message "Hello, FlyRank!"
- `/status` - Returns a JSON response with the status "ok" and the service name "my-first-api"

## How to run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to test

```bash
curl http://localhost:5000/
curl http://localhost:5000/status
```
