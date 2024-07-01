#!/bin/bash

# Define the project directory and build directory
PROJECT_DIR="$REPOS/ocaml"
PYTHON_SCRIPT="$(pwd)/benchmark_build.py"

# Run the benchmark Python script
$PYTHON_SCRIPT

