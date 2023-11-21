from io import BytesIO
import boto3
from bs4 import BeautifulSoup

def upload_html_to_s3(target, data:str):
    soup = BeautifulSoup(data, 'html.parser')
    soup_bytes = BytesIO(soup.encode('utf-8')).read()
    s3 = boto3.client(target['service'])
    s3.put_object(Body=soup_bytes, Bucket=target['detail_info']['bucket_name'], Key=target['detail_info']['object_key'])
    print("Data saved to S3")

def read_html_from_s3(target):
    s3 = boto3.client(target['service'])
    s3_response = s3.get_object(Bucket = target['detail_info']['bucket_name'], Key = target['detail_info']['object_key'])
    return s3_response['Body'].read().decode('utf-8')