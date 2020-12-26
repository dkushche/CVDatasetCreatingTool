#!/bin/bash

test -e webcam_env
if [[ "$?" -eq "1" ]]; then
    echo "Start installation process"
    python3 -m venv webcam_env
    source webcam_env/bin/activate
    pip install -r requirements.txt
    echo "Installed"
else
    echo "Already installed"
fi
