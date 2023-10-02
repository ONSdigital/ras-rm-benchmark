import os
from datetime import datetime

from scripts.google_cloud_storage import GoogleCloudStorage

'''
This script uploads the benchmark outputs to a GCS Bucket.
If running locally, you must specify valid Application Default Credentials (ADC):
https://cloud.google.com/docs/authentication/production
'''
if __name__ == '__main__':
    gcs_bucket_name = os.environ['GCS_BENCHMARK_RESULTS_BUCKET']

    if not gcs_bucket_name:
        raise ValueError(
            'Value for `GCS_BENCHMARK_RESULTS_BUCKET` environment variable not valid.'
        )

    host = os.getenv('HOST')
    output_directory = os.getenv('BENCHMARK_OUTPUT_DIRECTORY')
    # filename_prefix = os.getenv('OUTPUT_FILENAME_PREFIX')

    gcs = GoogleCloudStorage(bucket_name=gcs_bucket_name, directory=output_directory)
    gcs.upload_files(
        output_files=(
            'performance_graph.png',
            'summary.txt',
        ),
        directory=output_directory,
        # output_filename_prefix=filename_prefix,
        timestamp=int(datetime.utcnow().timestamp()),
    )
