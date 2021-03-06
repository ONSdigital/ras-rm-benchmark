import os
import json

from google.cloud import storage


class GoogleCloudStorage:
    def __init__(self, bucket_name, directory):
        self.project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
        self.bucket_name = bucket_name
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(self.bucket_name)
        self.directory = directory

    def upload_files(
        self, output_files, directory, output_filename_prefix=None, **kwargs
    ):
        for output_file in output_files:
            output_filename = (
                f'{output_filename_prefix}_{output_file}'
                if output_filename_prefix
                else output_file
            )

            blob = self.bucket.blob(f'{directory or ""}/{output_filename}')
            blob.metadata = {**kwargs}
            blob.upload_from_filename(filename=output_file)

    def get_files(self, from_date, output_dir):
        path = self.bucket_name
        for blob in self.client.list_blobs(path):

            if from_date and blob.time_created < from_date:
                continue

            file_path = blob.name.rsplit('/', 1)[0]

            output_file_path = f'{output_dir}/{file_path}'

            if not os.path.exists(output_file_path):
                os.makedirs(output_file_path)

            blob.download_to_filename(filename=f'{output_dir}/{blob.name}')

            metadata_file_path = f"{output_dir}/{file_path}/metadata.json"
            if not os.path.exists(metadata_file_path):
                with open(metadata_file_path, 'w+') as file:
                    file.write(json.dumps(blob.metadata, indent=2))
