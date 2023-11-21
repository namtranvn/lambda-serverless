import random
import psycopg2
import logging
import traceback
from bs4 import BeautifulSoup
import requests
import boto3
import csv
from io import BytesIO
from datetime import datetime
from common.db_utils import upload_html_to_s3, read_html_from_s3
from utils.crawl_news_in_day import crawl_url_news_in_day, crawl_news_inday

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def convert_date_format(input_date):
    # Parse the input date string
    date_object = datetime.strptime(input_date, '%Y/%m/%d')

    # Convert to the desired output format
    output_date = date_object.strftime('%-d/%-m/%Y')
    return output_date


def lambda_cafef_handler(event, context):
    try:
        link = f'https://cafef.vn/{event["topic"]}/{convert_date_format(event["date"])}'
        headers = event['headers']
        URLS = crawl_url_news_in_day(link, headers)
        for url in URLS:
            try:
                response = crawl_news_inday(url, headers)
                response_text = response.text
                soup = BeautifulSoup(response_text, 'html.parser')
                distribution_date = soup.find('input', {'id': 'distributionDate'})['value'].split('T')
                target = {
                  "service": "s3",
                  "detail_info": {
                    "bucket_name": "ai4e-ap-southeast-1-dev-s3-data-landing",
                    "object_key": f"raw_zone/thiemcun203/raw_html/cafef/{event['topic']}/{distribution_date[0]}_news/{distribution_date[1]}_news.html"
                    }
                  }

                upload_html_to_s3(target, response_text)
            except AssertionError as ex:
                logger.error(f'FATAL ERROR: {ex} at {url}')
                print(f'ERROR: {ex} at {url}')

        return {
            'statusCode': 200,
        }
    
    except AssertionError as ex:
        logger.error(f'FATAL ERROR: {ex}')
        return {"status": "FAIL", "error": str(ex), "url": link}
    
    except Exception as ex:
        logger.error(f'FATAL ERROR: {ex}')
        logger.error('TRACEBACK:')
        logger.error(traceback.format_exc())
        return {"status": "FAIL", "error": str(ex)}
    

