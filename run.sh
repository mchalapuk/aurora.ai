#!/bin/bash

VENV_DIR=".venv"
PYTHON=${PYTHON:-python3}

cd $(dirname $0)

test -d $VENV_DIR || $PYTHON -m venv --upgrade-deps $VENV_DIR
source $VENV_DIR/bin/activate

$PYTHON -m pip install -r requirements.txt
$PYTHON aurora/main.py

