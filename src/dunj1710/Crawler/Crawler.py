import requests
from bs4 import BeautifulSoup
import re
import time


class CrawlingDataTool:
    def __init__(self, link_file):
        # Initial setup
        self.link_file = link_file


    def create_features(self):
        return {
            'brand': [],
            'name': [],
            'price': [],
            'nam_sx': [],
            'origin': [],
            'type_car': [],
            'km_traveled': [],
            'gear': [],
            'condition': [],
            'fuel': [],
            'engine': []
        }

    def input_initial_features(self, data):
        for i in data.keys():
            data[i].append('None')

    def crawling_data(self):
        data = self.create_features()
        href_links = self.link_file
        
        for href_link in href_links:
            self.input_initial_features(data)
            try:
                response = requests.get(href_link)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Continue processing for this href_link
                    # Get name and brand
                    try:
                        name = soup.find('h1', {'class':'title-detail'}).text.strip()  # Example: Assuming the name is within an h1 tag with the given class
                        data['name'].pop()
                        data['brand'].pop()
                        data['name'].append(name.replace('\n','').replace('\r',''))
                        data['brand'].append(re.findall('(\w+)(?=\s)', name)[0])
                    except:
                        print("Error in getting name")
                        continue

                    # Get price
                    try:
                        data['price'].pop()
                        price = soup.find(class_='price').text.strip()
                        data['price'].append(price.replace('\n',''))
                    except:
                        print("Error in getting price")
                        continue

                    # Get all information from the box with the class 'list-info'
                    try:
                        info_list = soup.find(class_='list-info')
                        elements = info_list.find_all("li")
                        for element in elements:
                            label_text = element.find(class_='label').text
                            if "Năm SX" in label_text:
                                data['nam_sx'].pop()
                                data['nam_sx'].append(element.text.replace('\n', ' ').replace("Năm SX",''))

                            if "Kiểu dáng" in label_text:
                                data['type_car'].pop()
                                data['type_car'].append(element.text.replace('\n', ' ').replace("Kiểu dáng",''))

                            if "Tình trạng" in label_text:
                                data['condition'].pop()
                                data['condition'].append(element.text.replace('\n', ' ').replace("Tình trạng",''))

                            if "Xuất xứ" in label_text:
                                data['origin'].pop()
                                data['origin'].append(element.text.replace('\n', ' ').replace("Xuất xứ",''))

                            if  "Km đã đi" in label_text:
                                data['km_traveled'].pop()
                                data['km_traveled'].append(element.text.replace('\n', ' ').replace("Km đã đi",'')\
                                                        .replace('km','').replace('.',''))

                            if "Hộp số" in label_text:
                                data['gear'].pop()
                                data['gear'].append(element.text.replace('\n', ' ').replace("Hộp số",''))

                            if "Nhiên liệu" in label_text:
                                data['fuel'].pop()
                                data['fuel'].append(element.text.replace('\n', ' ').replace("Nhiên liệu",''))

                    except:
                        print("Error in getting info_list")
                        continue
                else:
                    print(f"Request for {href_link} returned status code {response.status_code}")

            except requests.RequestException as e:
                print(f"Request for {href_link} failed: {e}")

            time.sleep(1)
        
        print('done')
        return data
