#!/bin/bash

# Get benchmark outputs
GCS_OUTPUT_BUCKET="$GCS_OUTPUT_BUCKET" \
NUMBER_OF_DAYS="$NUMBER_OF_DAYS" \
pipenv run python -m scripts.get_benchmark_results

# Create performance graph
NUMBER_OF_DAYS="$NUMBER_OF_DAYS" \
pipenv run python -m scripts.visualise_results

# Date to get summary for
RUNTIME_DATE_STRING="$(date +'%Y-%m-%d')"
SUMMARY=$(OUTPUT_DIR="outputs/${OUTPUT_DIR}" \
OUTPUT_DATE="$RUNTIME_DATE_STRING" \
pipenv run python -m scripts.get_summary)

pipenv run python -m scripts.store_benchmark_outputs