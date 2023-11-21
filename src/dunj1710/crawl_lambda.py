from src.dunj1710.Crawler.Crawler import CrawlingDataTool
import logging
import traceback
import boto3
import csv

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
s3_client = boto3.client('s3')
s3_bucket_name = "ai4e-ap-southeast-1-dev-s3-data-landing"
s3_object_key = "raw_zone/dunj1710/used_car/used_car_data.csv"


def write_csv_to_s3(data, s3_bucket, s3_object_key):
    # Prepare CSV data
    csv_content = '\n'.join([','.join(map(str, row)) for row in zip(*data.values())])

    # Upload the CSV file to S3
    s3_client.put_object(Body=csv_content.encode('utf-8'), Bucket=s3_bucket, Key=s3_object_key)

def lambda_handler(event, context):
    try:
        logger.info(f"EVENT: {event}")
        logger.info(f"CONTEXT: {context}")
        link_file = event['urls']


        # Create an instance of your Crawling_data_tool class
        crawler = CrawlingDataTool(link_file)

        # Gather the data
        data = crawler.crawling_data()

        # Write the data to S3
        # Ghi dữ liệu xuống S3 bucket
        write_csv_to_s3(data, s3_bucket_name,s3_object_key)

        return {"status": "SUCCESS",}
    except Exception as ex:
        logger.error(f'FATAL ERROR: {ex}')
        logger.error('TRACEBACK:')
        logger.error(traceback.format_exc())

        return {"status": "FAIL", "error": f"{ex}", "message": "Error occurred. Check logs for more details."}