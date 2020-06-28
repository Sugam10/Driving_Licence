from selenium import webdriver
import urllib


driver = webdriver.Chrome("C:/Users/Sumedha/Downloads/chromedriver.exe")
driver.get("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")




# Download image/captcha.
img = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt32:j_idt38"]')
src = img.get_attribute('src')
urllib.request.urlretrieve(src, "captcha.jpeg")


