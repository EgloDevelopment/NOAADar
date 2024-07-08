#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Installing Python..."
    sudo apk update
    sudo apk add python3
else
    echo "Python is already installed."
fi

# Check if NPM is installed
if ! command -v npm &> /dev/null; then
    echo "NPM is not installed. Installing NPM..."
    sudo apk update
    sudo apk add npm
else
    echo "NPM is already installed."
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Installing Node.js..."
    sudo apk add curl
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E sh -
    sudo apk add nodejs
else
    echo "Node.js is already installed."
fi

# Install pm2 globally
if ! command -v pm2 &> /dev/null; then
    echo "pm2 is not installed. Installing pm2 globally..."
    sudo npm install -g pm2
else
    echo "pm2 is already installed."
fi

# Save before starting
pm2 save

# Start application
echo "Starting application using pm2"
pm2 start main.py --name "NOAADar" --no-autorestart --instances 1 --cron "*/10 * * * *"

# Save process list
pm2 save --force

# Set pm2 to startup on system boot
pm2 startup