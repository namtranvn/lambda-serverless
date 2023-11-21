

import os
import sys


# Getting to the Lambda directory
# sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))
sys.path.append()
# from src.ai4e_crawler.crawler import lambda_handler
from crawl_news import lambda_cafef_handler

event = {
'headers' : [{
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'laravel_session=eyJpdiI6IklScVh4SFlYUDJzZ0dxYjNmTFRmS1E9PSIsInZhbHVlIjoiaXU1WHFlUmNubXh0VUZJdG5iUGROeVFwcXd1dHp4VmZCQkxRbmF0K0ZsNHRkdUcvVUFKdnFRMkk1SnZyd0hYWnBSN3RCUWY0ZWRPZVUyeTgyMWg2OWJTYnJTbStqOXpZb3JwOWVGYzRKSXlnUWNvUzdpT2hMM2dmalE0SVFHcjMiLCJtYWMiOiIxM2UyZTk1MTE3NDk3OTZjYTk4MWE3ZmFkZDhjMWYwODJhYjYzZDM5YzFkYmEyMzVmNGZlODBjYThlZDk2NjQ4IiwidGFnIjoiIn0%3D; __uidac=01654a95e024ac52f1b3fc6dd9c7d949; dtdz=f82c714a-2b88-41f8-b598-f016ca67a264; favorite_stocks_state=1; _ga_860L8F5EZP=GS1.1.1699386848.1.0.1699386848.0.0.0; _ga=GA1.2.1459586384.1699386848; _gid=GA1.2.859278845.1699386849; _gat_gtag_UA_34575478_17=1; _uidcms=1699386849646799069; __RC=4; __R=1; __uif=__uid%3A6193868521953464045%7C__ui%3A-1%7C__create%3A1699386852; laravel_session=eyJpdiI6Ii8ySEVwU1ZTaHMyRzNjSEU5QnphOHc9PSIsInZhbHVlIjoiMVozSUJJRnQxZmM2TmhPTUZwVlgxRHVjQW5uUDJwRW1UWTV2Y3dKekhkRXhYZ1VSNWtLSmtLTnhvU1pMcEJIcE1UUm56VXBLN3l3RDh4OURlRlFjY0RkNE5HU0gzRGZSMTNUVEYwM2ZPZzNlSCt4UWlYV2tHdlpiYlFaZWZPek4iLCJtYWMiOiI0MzE0NzFiZjZkYTNmMjE2ZTM4ODJhZmVkNzhkNjBiZTM5ZmZiZWQ2NzFmNzQ5OTg3NzRkZGE2Zjc0YTk3YzZkIiwidGFnIjoiIn0%3D',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55',
        'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    },
    {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    'Cookie': '__R=0; __RC=134031; __uif=__uid%3A5393878981746696063%7C__ui%3A-1%7C__create%3A1699387898; laravel_session=eyJpdiI6InFGdEZVRGZyL3h6Mkh2blh3aE8wQUE9PSIsInZhbHVlIjoiUHVVY2VKZElzMXBDQzBjR2lOQUxQOUZWRWl1WlcvVDlTbi8yRUhKaEJoQS9kODRjVkxsV2RMTXZMUnY0cmVPa3YvQWRzME8wZlE4QzQ2dEdHY1htZDJmaEsxa0crTTRtTHZBOGladFpUVHIzTzZQR1hUYktGenVOVS9nNDVsYzgiLCJtYWMiOiJlNGUyMTgxYjY5YTg1MDNkNTAwZjk0NGZmMWZmY2ZhMTc5NjY5MjIzYmZkZjI0ZWFiYmU1ODM2ZGMzMTM0YjljIiwidGFnIjoiIn0%3D; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%223ab72e6f-e936-95db-1417-ab8e0f4b12f0%22%2C%22e%22%3A2199387899091%2C%22c%22%3A1699387889353%2C%22l%22%3A1699387899091%7D; favorite_stocks_state=1; _ga=GA1.1.600939006.1699387898; _ga_860L8F5EZP=GS1.1.1699387897.1.0.1699387897.0.0.0; _uidcms=1699387897575109840; dtdz=a86b8573-459f-4b5e-8253-4ae23013218c; __uidac=01654a99f14fb1fd89d045731786eccf; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22c173819a-2899-b4ef-ab81-802be9da64c0%22%2C%22c%22%3A1699387889353%2C%22l%22%3A1699387889353%7D; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%222283007%22%2C%22c%22%3A1699387889353%2C%22l%22%3A1699387889353%7D; laravel_session=eyJpdiI6Ii8ySEVwU1ZTaHMyRzNjSEU5QnphOHc9PSIsInZhbHVlIjoiMVozSUJJRnQxZmM2TmhPTUZwVlgxRHVjQW5uUDJwRW1UWTV2Y3dKekhkRXhYZ1VSNWtLSmtLTnhvU1pMcEJIcE1UUm56VXBLN3l3RDh4OURlRlFjY0RkNE5HU0gzRGZSMTNUVEYwM2ZPZzNlSCt4UWlYV2tHdlpiYlFaZWZPek4iLCJtYWMiOiI0MzE0NzFiZjZkYTNmMjE2ZTM4ODJhZmVkNzhkNjBiZTM5ZmZiZWQ2NzFmNzQ5OTg3NzRkZGE2Zjc0YTk3YzZkIiwidGFnIjoiIn0%3D',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'cafef.vn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Sec-Fetch-Dest': 'document',
    'Connection': 'keep-alive'
    },
    {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'none',
    'Cookie': '_uidcms=1699387974349638813; favorite_stocks_state=1; dtdz=49aa73ac-99bf-4fba-bbe7-c7e2862b4ad4; __uidac=01654a9a3f23dd6e9790c481ae4f9dfc; laravel_session=eyJpdiI6Ii8ySEVwU1ZTaHMyRzNjSEU5QnphOHc9PSIsInZhbHVlIjoiMVozSUJJRnQxZmM2TmhPTUZwVlgxRHVjQW5uUDJwRW1UWTV2Y3dKekhkRXhYZ1VSNWtLSmtLTnhvU1pMcEJIcE1UUm56VXBLN3l3RDh4OURlRlFjY0RkNE5HU0gzRGZSMTNUVEYwM2ZPZzNlSCt4UWlYV2tHdlpiYlFaZWZPek4iLCJtYWMiOiI0MzE0NzFiZjZkYTNmMjE2ZTM4ODJhZmVkNzhkNjBiZTM5ZmZiZWQ2NzFmNzQ5OTg3NzRkZGE2Zjc0YTk3YzZkIiwidGFnIjoiIn0%3D',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'cafef.vn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Sec-Fetch-Dest': 'document',
    'Connection': 'keep-alive'
    },
    {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__uidac=01654a9aa1412f87dd1fbc2e3f2a1677; favorite_stocks_state=1; _ga_860L8F5EZP=GS1.1.1699388066.1.0.1699388066.0.0.0; laravel_session=eyJpdiI6Im5PMFh2Y3VNWDN6TWEzTG5TaUU2RHc9PSIsInZhbHVlIjoiaVZTT3B1aFJlaVFZZ1MvSjZocU1PR2V1UXUwK3RrY1hZYnllOTZ1aEhPeWh2UUlibDMwd253SkVyM1ZlSDA1bnRNRFRpOE9MZjM3a3JVTXlBQzdsUEtSaXJVNkxURS9NeUxtdzNQZ1UydkdmSzU2S1EwcjR5Qmp5Yk1zbDU4bEkiLCJtYWMiOiJlZjhiNzUwNjYwMTNjNmU2MDFmM2E2MzBjNmFjNGI2ODE1YWY5ODc4NjM1NWIxOTAxOTJiMDQxNDIzMjEwMTA5IiwidGFnIjoiIn0%3D; dtdz=27d14f45-981b-4b64-93d5-3f9f43021c0e; _ga=GA1.2.976762088.1699388066; _gid=GA1.2.681797149.1699388066; _gat_gtag_UA_34575478_17=1; laravel_session=eyJpdiI6Ii8ySEVwU1ZTaHMyRzNjSEU5QnphOHc9PSIsInZhbHVlIjoiMVozSUJJRnQxZmM2TmhPTUZwVlgxRHVjQW5uUDJwRW1UWTV2Y3dKekhkRXhYZ1VSNWtLSmtLTnhvU1pMcEJIcE1UUm56VXBLN3l3RDh4OURlRlFjY0RkNE5HU0gzRGZSMTNUVEYwM2ZPZzNlSCt4UWlYV2tHdlpiYlFaZWZPek4iLCJtYWMiOiI0MzE0NzFiZjZkYTNmMjE2ZTM4ODJhZmVkNzhkNjBiZTM5ZmZiZWQ2NzFmNzQ5OTg3NzRkZGE2Zjc0YTk3YzZkIiwidGFnIjoiIn0%3D',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
    },
            
    ],
'date': '2023/11/11',
# 'topic':'thi-truong-chung-khoan',
  'topic':'doanh-nghiep',

}

lambda_cafef_handler(event, None)