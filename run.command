#!/bin/bash

cd "$(dirname "$0")"

echo "Current folder:"
pwd

echo ""
echo "Starting Food Tracker..."
echo ""

python3 ./main.py

echo ""
read -p "Press Enter to close..."