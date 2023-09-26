import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import lxml
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get("https://www.hepsiemlak.com/isparta-kiralik/isyeri",headers=header)
data = response.text
soup = BeautifulSoup(data, "lxml")
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSdqC0AbcsudYbn5rCww6MgXn691qYDHc4Rk7RmO3idme1b9Dw/viewform?usp=sf_link")
all_price_elements = soup.select(".list-view-price")
prices=[]
for link in all_price_elements:
    price=link.text
    price=price.replace("TL","").replace(".","")
    prices.append(int(price.strip(" \n")))

all_describe_elements=soup.select(".list-view-header")
describes=[]
for inside in all_describe_elements:
    describes.append(inside.text.strip(" \n").replace("",''))
print(describes)
# print(describes)
# all_link_elements=soup.find_all(class_=".links",href=True)
# print(all_link_elements)
all_link_elements=soup.select(".links a[href]")
# print(all_link_elements)
all_links=[]
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.hepsiemlak.com{href}")
    else:
        all_links.append(href)


for i in range(len(all_link_elements)):
    driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSdqC0AbcsudYbn5rCww6MgXn691qYDHc4Rk7RmO3idme1b9Dw/viewform?usp=sf_link")
    describe_input = driver.find_element(By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    salary_input = driver.find_element(By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    time.sleep(2)
    salary_input.send_keys(prices[i])
    describe_input.send_keys(describes[i])
    link_input.send_keys(all_links[i])
    submit.click()
    time.sleep(2)

