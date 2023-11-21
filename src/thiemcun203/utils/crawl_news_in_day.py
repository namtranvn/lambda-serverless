import time
import requests
from bs4 import BeautifulSoup
import random

def crawl_url_news_in_day(origin_url:str, headers:list) -> list:
    '''Function to crawl all url news in specific day from CafeF'''
    URLS = []
    next = True
    i=1
    while next:
        #request to get html
        url = origin_url + f'/trang-{i}.chn'  # Replace with the actual URL you want to scrape
        HEADERS = random.choice(headers)
        response = requests.get(url,
                                headers=HEADERS,
                                )
        sleep_rate = 0.2
        while True:
            #check request parent page
            if response.status_code == 200:
                print(f"Scraping URL: {url}")
                soup = BeautifulSoup(response.text, 'html.parser')
                #move to next page?
                next = soup.find(class_="pagination-next")
                
                # Extract the content of the HTML document
                elements = soup.find_all(class_='tlitem box-category-item')
            
                # Open the CSV file in write mode
                for element in elements:
                    link = 'https://cafef.vn' + element.find('a')['href']   
                    URLS.append(link)
                break
            elif response.status_code == 404:
                time.sleep(sleep_rate)
                if sleep_rate > 5:
                    assert False, f"Failed to retrieve data from the parent website {response.status_code}"
                sleep_rate += 1
            else:
                assert False, f"Failed to retrieve data from the parent website {response.status_code}"
        i += 1
    return URLS
def crawl_news_inday(url:str, headers:str):
    '''Function to crawl news from CafeF in day based on specific in url list'''
    HEADERS = random.choice(headers)
    response = requests.get(url, headers=HEADERS)
    sleep_rate = 0
    while True:
            #check request parent page
            if response.status_code == 200:
                print(f"Scraping URL: {url}")
                return response
            elif response.status_code == 404:
                time.sleep(sleep_rate)
                if sleep_rate > 5:
                    assert False, f"Failed to retrieve data from the parent website {response.status_code}"

                sleep_rate += 1
            else:
                assert False, f"Failed to retrieve data from the parent website {response.status_code}"
        
    
if __name__ == '__main__':
    headers = [{
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
        }]
    URlS = crawl_url_news_in_day('https://cafef.vn/thi-truong-chung-khoan/5/11/2023', headers)
    print(crawl_news_inday(URlS[0], headers).text[:1000])
    
    