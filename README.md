# ras-rm-benchmark
A benchmarking tool for RASRM

This repository was heavily inspired by the [eq survey runner benchmark](https://github.com/ONSdigital/eq-survey-runner-benchmark).

**TODO**: The following will be improved before merging and is just to capture useful commands in the interim

```bash
cd <YOUR_PARTH>/ras-rm-benchmark

export NUMBER_OF_DAYS=10
export RUNTIME_DATE_STRING="$(date +'%d-%m-%y-%H-%M')"
export GCS_OUTPUT_BUCKET=ras-rm-performance-20220908-results
export GCS_BENCHMARK_RESULTS_BUCKET=ras-rm-performance-20220908-benchmark
export BENCHMARK_OUTPUT_DIRECTORY=$RUNTIME_DATE_STRING
export OUTPUT_DIR="outputs/"

rm -rf outputs
rm performance_graph.png
rm summary.txt

# Run this script after setting the above vars

./process-results.sh

# Or you can run the scripts separately for dev purposes, after setting the above vars

pipenv run python -m scripts.get_summary
pipenv run python -m scripts.visualise_results
pipenv run python -m scripts.store_benchmark_outputs

open performance_graph.png
```
