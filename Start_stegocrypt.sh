#!/bin/bash

Generate a random port between 5000 and 9000

PORT=$((RANDOM % 4000 + 5000)) export PORT=$PORT

echo "Starting StegoCrypt on port $PORT..."

Start the server with the same random port

python3 stegocrypt.py

