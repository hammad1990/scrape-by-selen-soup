from selenium import webdriver
##from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
##from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import lxml
import pandas as pd
from time import sleep


image_list=[]
Title_list=[]
author_list=[]
date_published=[]  #not available at site
desc_list=[]
price_list=[]
books_list=[]

for page_number in range (1,56):
    url=f"https://www.buchhandel.de/fachzeitschriften?page={page_number}&pageSize=100"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='C:/Users/User DW/Downloads/chromedriver', options=chrome_options)


    driver.get(url)
    sleep(6)

    soup=BeautifulSoup(driver.page_source,'lxml')
    ##print(soup.prettify())
##    title=soup.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.p.span.a.text
##    print(title)

    trs=soup.find_all('tr',class_='table_row')
##    print(len(trs))

    for tr in range (0,len(trs)):
        if page_number==1:
            if tr==0:
                image_list.append(trs[tr].td.div.img['src'])
                Title_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.p.span.a.text)
                author_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.contents[1].text.strip())
                desc_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.contents[1].contents[5].text)
                price_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.span.text)
                books_list.append([image_list[tr],Title_list[tr],author_list[tr],desc_list[tr],price_list[tr]])
            else:
                image_list.append(trs[tr].td.div.img['src'])
                Title_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.p.span.a.text)
                author_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.contents[3].text.strip())
                desc_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.contents[1].contents[5].text)
                price_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.span.text)
                books_list.append([image_list[tr],Title_list[tr],author_list[tr],desc_list[tr],price_list[tr]])
        else:
                image_list.append(trs[tr].td.div.img['src'])
                Title_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.p.span.a.text)
                author_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.contents[3].text.strip())
                desc_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.contents[1].contents[5].text)
                price_list.append(trs[tr].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.p.span.text)
                books_list.append([image_list[tr],Title_list[tr],author_list[tr],desc_list[tr],price_list[tr]])
            


    print("page number"+"="+str(page_number))
    sleep(6)
df=pd.DataFrame(books_list,columns=['image URL','Title','Author','Description','Prices'])
                          

##    print(df.to_string())
df.to_csv('books_new.csv')
driver.quit()


