from django.shortcuts import render
from django.shortcuts import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def index(request):
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://perfumancebd.com/product-category/perfume/refreshing/")

    
    total_food = 4*2+3

    title_list = []
    # imge_list = []
    # price_list = []

    for i in range(1, total_food+1):

        x_path = '//*[@id="rig-adpr"]/div['+str(i)+']/p[1]'

        # img = '//*[@id="rig-adpr"]/div[1]/a/img'

        # pric = '//*[@id="rig-adpr"]/div['+str(i)+']/p[2]'


        print(x_path)

        title = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, x_path)))

        # imge = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, img)))

        # price = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, pric)))

        title_list.append(title.text)
        # imge_list.append(imge.get_attribute('src'))
        # price_list.append(price.get_attribute('innerHTML'))
    print("product title:",title_list)

    love = {"title":title_list,"price":100}

    return render(request, 'parfume _1/form.html',context=love)
   



    #print("product image:", imge_list)

    #print("product price:", price_list)


    
    
    
    





# Create your views here.