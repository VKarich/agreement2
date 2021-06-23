from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get("https://rosreestr.gov.ru/wps/portal/online_request")
cad_num = driver.find_element_by_name("cad_num")
cad_num.clear()
cad_num.send_keys("63:01:0109006:3387")
cad_num.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 1).until(
    lambda x: x.find_element_by_id("td"))

tds = driver.find_elements_by_class_name("td")
tds[0].find_element_by_xpath("a").click()

#button = driver.find_element_by_id("submit-button")
#button.click()
