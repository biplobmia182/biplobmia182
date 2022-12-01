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

    x_path = '//*[@id="rig-adpr"]/div[1]/p[1]'


    title = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, x_path))).text

    love = {"title":title, "price":100}

    #return HttpResponse(title)
    return render(request, 'rokomari/form.html',context=love)


# Create your views here.