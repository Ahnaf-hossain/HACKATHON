# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Md Ahnaf Abid Hossain
# Section:      528
# Assignment:   THE ASSIGNMENT NUMBER (e.g. Lab 1b-2)
# Date:         DAY MONTH YEAR
#

#
# YOUR CODE HERE
#


from selenium import *


from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager



import time



from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def getTextFile(bookName):
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    
    
    
    
    
    
    
    
    
    
    
    driver = webdriver.Chrome(ChromeDriverManager().install(),options = options)
    driver.get("https://gutenberg.org")
    driver.maximize_window()
    search = driver.find_element_by_class_name("searchInput")
    search.click()
    search.send_keys(bookName)
    search = driver.find_element_by_name("submit_search")
    search.click()
    s = driver.find_elements_by_css_selector("span[class= 'title']")
    ratio = []
    for i in s:
        print(i.text)
        ratio.append(fuzz.ratio(bookName , i.text))
        
    print(ratio)
    index = ratio.index(max(ratio))
    
    
    
    s[index].click()
    search = driver.find_element_by_link_text("Plain Text UTF-8")
    search.click()
            
    
            




    url = driver.current_url

    print(url)


    '''
    from urllib.request import urlopen
    page = str(urlopen(url).read())
    
    
    
    rendered_content = html2text.html2text(page)
    print(rendered_content)
    file = open('file_text.txt', 'w')
    file.write(rendered_content)
    file.close()
    '''
    
    import requests
    
    r = requests.get(url, allow_redirects=True)
    
    file = open('facebook.txt', 'wb')
    file.write(r.content)
    file.close()
    
