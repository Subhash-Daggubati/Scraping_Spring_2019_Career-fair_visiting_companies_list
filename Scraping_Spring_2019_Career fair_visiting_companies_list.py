# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:29:47 2019

@author: subha
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os


os.chdir('D:\Spring 2019')


driver = webdriver.Chrome("D:\\Summer 2019\\Anil\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.hireosugrads.com/StudentsAlumni/Event-STEM.aspx")

newrows =[]

base_xpath_link = "//*[@id=\"EventsEmployerTable\"]/tbody/tr["
tail_xpath_link = "]/td[1]/a"
list_size = len(driver.find_elements_by_xpath("//*[@id=\"EventsEmployerTable\"]/tbody/tr")) #extract the entire list of company links

for j in range(list_size-2):
    if(j<67): 
        xpath_link = base_xpath_link + str(j+2) + tail_xpath_link #used to skip the non working link.
    else:
        xpath_link = base_xpath_link + str(j+3) + tail_xpath_link
    elem = driver.find_element_by_xpath(xpath_link)
    window_before = driver.window_handles[0]
    elem.click()  #Click on the link of each company coming for career fair. This will open a new tab with all the details of the company and positions available at the company
    window_after = driver.window_handles[j+1]
    driver.switch_to_window(window_after) #switch the driver to new window that was opened.
    length = len(driver.find_elements_by_xpath("/html/body/div[1]/div/table/tbody/tr"))
    base_xpath ="/html/body/div[1]/div/table/tbody/tr["
    tail_xpath="]/th"
    tail_xpath_data = "]/td"
    header = "NA"
    info ="NA"
    row_dic = {}
	#from the company details page each and every row from the table will be extracted and stored into row_dic, dictionary variable with column header as key and the data as value.
    for i in range(length):
        xpath=base_xpath+str(i+1)+tail_xpath
        xpath_data=base_xpath+str(i+1)+tail_xpath_data
        th_elem= driver.find_element_by_xpath(xpath)
        td_elem= driver.find_element_by_xpath(xpath_data)
        header = th_elem.text
        info = td_elem.text
        new_row = {header:info}
        row_dic.update(new_row)    
    newrows.append(row_dic)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL +"w")
    driver.switch_to_window(window_before)    #Once all the details of a company are captured in the dictionary driver will be pointed back to the main page where the companies list is provided and the process will be repeated with the next company
data = pd.DataFrame(newrows)  
data.to_csv("Career Fair2.csv") #Extract the data into excel sheet.

driver.close()  