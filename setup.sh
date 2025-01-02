#!/bin/bash
set -e  # Exit on error

echo "Starting setup..."

# Stop any existing containers
docker compose down

# Start containers
docker compose up -d

echo "Setup complete! Arduino port is ready."
