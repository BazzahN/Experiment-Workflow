#!/bin/bash

CONFIG=$1 #Experiment name yml suffix and folder is added automatically
source ./activate_env
echo "============================"
echo "Running Experiment: $CONFIG"
echo "============================"

#Script executed with config argument using the python package argparse
python experiment.py --config "configs/$CONFIG.yml"

echo "done"
