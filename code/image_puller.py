import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def get_smallimage_url(keyword):
    url = f"https://www.bing.com/images/search?q={keyword}&first=1"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    divs = soup.find_all("div", class_="img_cont hoff")
    sources = []
    for div in divs:
        # Her bir div içindeki img etiketlerini bul
        img_tags = div.find_all("img")
        for img_tag in img_tags:
            # img etiketinin src özniteliğini almaya çalış
            src = img_tag.get("src")
            sources.append(src)
            # Eğer src özniteliği yoksa, başka bir öznitelikten (örneğin data-src) URL'yi almaya çalış
            if src is None:
                src = img_tag.get("data-src")
                sources.append(src)
            # Eğer hala URL bulunamadıysa, bu img etiketini atla ve bir sonrakine geç
            if src is None:
                continue
            # Her bir img etiketinin src özniteliğini yazdır
            # print("Image URL:", src)

    return sources

def get_linkimage_url(keyword):
    url = f"https://www.bing.com/images/search?q={keyword}&first=1"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    divs = soup.find_all("ul", class_="b_dataList")
    
    real_urls = []
    for div in divs:
        # Her bir div içindeki img etiketlerini bul
        img_tags = div.find_all("a")
        for img_tag in img_tags:
            # img etiketinin src özniteliğini almaya çalış
            src = img_tag.get("href")
            real_urls.append("https://www.bing.com"+src)
            # Eğer src özniteliği yoksa, başka bir öznitelikten (örneğin data-src) URL'yi almaya çalış
            if src is None:
                src = img_tag.get("href")
                real_urls.append("https://www.bing.com"+src)
            # Eğer hala URL bulunamadıysa, bu img etiketini atla ve bir sonrakine geç
            if src is None:
                continue
            # Her bir img etiketinin src özniteliğini yazdır
            # print("Image URL:", "https://bing.com/"+src)
    
    return real_urls



def get_downloadimage_url(photoUrl):
    url = photoUrl
    driver = webdriver.Chrome()
    driver.get(url)
    
    time.sleep(5)

    security = driver.find_element(By.XPATH, "//*[@id='bnp_btn_accept']")
    security.click()
    time.sleep(2)

    büyükresim = driver.find_element(By.XPATH, "//*[@id='actionbar']/ul/li[3]/div")
    büyükresim.click()

    # Yeni sekmenin açılmasını bekle
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    
    # Tüm açık pencerelerin ID'lerini al
    window_handles = driver.window_handles
    
    # Yeni sekmenin ID'sini al
    new_window_handle = [handle for handle in window_handles if handle != driver.current_window_handle][0]
    
    # Yeni sekmenin penceresine geçiş yap
    driver.switch_to.window(new_window_handle)

    print(driver.current_url)

    
    response = requests.get(driver.current_url)

    with open("photo.jpg", "wb") as f:
        f.write(response.content)
        time.sleep(5)

    