#!/bin/bash

# Update and install any necessary packages
apt-get update && apt-get install -y sqlite3

# Run the application setup if needed
python main.py

