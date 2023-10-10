# ras-rm-benchmark
A benchmarking tool for RASRM.

This repository was heavily inspired by the [eq survey runner benchmark](https://github.com/ONSdigital/eq-survey-runner-benchmark).

Poorly named, this tool does not carry out any benchmarking of RASRM's performance. Its sole purpose is to create a time series `summary.txt` and `performance_graph.png` from the sets of [Locust performance test](https://github.com/ONSdigital/ras-rm-performance-tests) output files.

To illustrate its use, the following commands can be used to run or test locally. Ensure you have authenticated your gcloud account as these scripts require access to the `locust` and `benchmark` GCP buckets.

```bash
cd <YOUR_PARTH>/ras-rm-benchmark

# set the variables for the run
export NUMBER_OF_DAYS=10
export RUNTIME_DATE_STRING="$(date +'%y-%m-%d-%H-%M')"
export GCS_OUTPUT_BUCKET=ras-rm-performance-20220908-locust
export GCS_BENCHMARK_RESULTS_BUCKET=ras-rm-performance-20220908-benchmark
export BENCHMARK_OUTPUT_DIRECTORY=results
export OUTPUT_DIR="outputs/"

# Remove any previous runs
rm -rf outputs
rm performance_graph.png
rm summary.txt

# Run the complete process to fetch the Locust files and generate the summary and graph
./process-results.sh

# Or you can run the scripts separately for dev purposes
pipenv run python -m scripts.get_summary
pipenv run python -m scripts.visualise_results
pipenv run python -m scripts.store_benchmark_outputs

# View the result files created in the application root directory
cat summary.txt
open performance_graph.png
```
