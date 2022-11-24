from selenium import webdriver
import time

driver = webdriver.Chrome()


first_url= 'http://c.biancheng.net'
driver.get(first_url)
time.sleep(2)

second_url='http://c.biancheng.net/c/'
driver.get(second_url)
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)


driver.refresh() 
time.sleep(2)

driver.quit()
