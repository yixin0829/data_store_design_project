from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re #Regular Experssion library 
import time
from bs4 import BeautifulSoup
import urllib.request 
import pandas as pd

"""
driver = webdriver.Chrome(executable_path=r'C:\\Users\\yixin\\Downloads\\chromedriver_win32\\chromedriver.exe')

#Establish session on with Chrome 
link = 'https://www.youtube.com/watch?v=TPpoJGYlW54'
driver.get(link)
time.sleep(2)
#Validate the link being used
print('\nUsing link: ' + link + '\n')

#Create soup object parsing using lxml (third-party lib)
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify()[:100])

#Getting text data for the comments 
text_from_websource = soup.get_text()

#Find all elements that have attribute of a comments (In this case we chooose a video on youtube with most views)
comments = soup.find_all(attrs={'id': 'content-text'})
print(comments)

"""

with urllib.request.urlopen('https://www.youtube.com/watch?v=TPpoJGYlW54') as response:
    html = response.read()

#Createing the soup
soup = BeautifulSoup(html, 'lxml')

#Preview the first 100 characters
print(soup.prettify()[:100])

#Getting text data from a parse tree
text_only = soup.get_text()
""" Issue: doesn't print since Youtube comments session need to be triggered by users" (might need selenium in here)""" 
comments = soup.find_all(class_ = "style-scope ytd-comment-renderer")

#Create a suedo comments list instead
comments = []
for i in range(100):
    comments.append("Hate speech is usually thought to include communications of animosity or disparagement of an individual or a group on account of a group characteristic such as race, color, national origin, sex, disability, religion, or sexual orientation.")



#Write into .csv file
filename  = "youtube_comments.csv"
f = open(filename, "w")

headers = "comment\n"
#Collect comments and import into .csv file
f.write(headers)

#Loop through all elements in the HTML and scrap user comments
user_idx = 0
for comment in comments:
    f.write(comment.replace(",", " "))
    f.write("\n")
    print('importing comment' + str(user_idx))
    user_idx +=1

f.close()