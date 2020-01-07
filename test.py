import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc_func(number):
    return str(math.log(math.fabs(12 * math.sin(int(number)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    driver = webdriver.Chrome()
    driver.get(link)

    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    driver.find_element_by_id('book').click()

    num = driver.find_element_by_xpath('//span[@id="input_value"]').text
    result = calc_func(num)

    input = driver.find_element_by_tag_name('input')
    input.send_keys(result)

    driver.find_element_by_id('solve').click()
finally:
    time.sleep(10)
    driver.quit()

