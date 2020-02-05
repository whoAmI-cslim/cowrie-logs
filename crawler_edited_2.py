### imports ###

import sys
import os
import requests 
import json
from bs4 import BeautifulSoup 
import csv
import pandas as pd
from secrets2 import USRName, Passwd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

### Yahoo Finance Login Op ###
def yahoo_login(url = 'https://finance.yahoo.com/screener/bbbf9769-a26a-4813-a13c-d227a336a693'):
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(executable_path='geckodriver', options=options)

    browser.get(url)

    emailElem = browser.find_element_by_id('login-username')
    emailElem.send_keys(USRName)

    loginbtn=browser.find_element_by_id("login-signin")
    loginbtn.click()

    passwordElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "login-passwd")))
    passwordElem.send_keys(Passwd)

    submitBtn=browser.find_element_by_id("login-signin")
    submitBtn.click()
    time.sleep(2)

### Update data every 5 seconds ###
def organize_data(html):
    html = browser.page_source
    organize_data(html)
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.findAll('table', {"class" : 'W(100%)'})
    
    flat_list = []
    for table in tables:
        table_headers = table.find('thead')
        headers = table_headers.find_all('th')
 
        for header in headers:  
            col_head = header.find_all('span')
            col_head = [cell.text.strip() for cell in col_head]
            for item in sublist:
                flat_list.append(item)
    
    columns=["Symbol", 'Names', 'Prices', 'Change','Change Percentage']
    df_ = pd.DataFrame(columns)
    
    for table in tables:
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:     
            col_val = row.find_all('td')
            col_val = [cell.text.strip() for cell in col_val]
            df_.append(col_val)
    
    time.sleep(4)
    display (df)




### main section ###

def main():
    yahoo_login()# you can give it an url as parameter
    #update and organize data 5 times, with 5 second intervals
    for i in range(1, 5):
        print("updating data")
        organize_data()
        time.sleep(5)

    browser.quit()

if __name__ == "__main__":
    main()

### end of program ###

