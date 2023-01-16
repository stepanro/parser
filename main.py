from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

brouser.get('https://www.avito.ru/')

find = brouser.find_element_by_class('input-input-Zpzc1').send_keys('mi band')
click = brouser.find_element_by_class('desktop-1jh0ioo').click()

print(find)
print(click)