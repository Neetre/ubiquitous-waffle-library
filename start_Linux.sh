#!/bin/bash

source ./setup/setup_Linux.sh

echo "LAN IP? (y/n):"
read UserInput

cd /bin/

if [ $UserInput = "n" ]; then
    python3 webpage.py --local
    exit
fi

python3 webpage.py --ip
exit