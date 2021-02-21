#!/bin/bash

set -e

VENVS_PATH=./venvs

pip install grpcio-tools

function setup_python_env() {
    reqs=$1     # boolean
    venvName=$2 # string
    rootName=$3 # string
    cd $VENVS_PATH
    python -m venv --clear $venvName
    source ./$venvName/bin/activate
    cd ../$rootName
    if $reqs
    then
        pip install -r requirements.txt
    else
        pip install .
    fi
    deactivate
    cd ..
}


CALL :SetupEnv 1 , venv1 , root1
CALL :SetupEnv 1 , venv2 , root2
CALL :SetupEnv 1 , venv_common , shared_lib

setup_python_env true "venv1" "root1"
setup_python_env true "venv2" "root2"
setup_python_env true "venv_common" "shared_lib"
