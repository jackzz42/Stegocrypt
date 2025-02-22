#!/bin/bash

Generate a random port between 5000 and 9000

PORT=$((RANDOM % 4000 + 5000)) export PORT=$PORT

Generate a random encryption key for extra security

export SECRET_KEY=$(openssl rand -hex 16)

echo "Starting StegoCrypt on port $PORT with enhanced security..."

Start the server with the randomized port and encryption key

python3 stegocrypt.py

