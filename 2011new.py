from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    # открытие страницы
    browser.get(link)

    # нажать на кнопку
    num1 = browser.find_element(By. CLASS_NAME, "btn.btn-primary")
    num1.click()

    num2 = browser.switch_to.alert #переключаемся на Alert
    num2.accept() #нажимаем ок

    num3 = browser.find_element(By. ID, "input_value")
    x = str(num3.text)
    print(x)
    otvet = calc(x)
    print(otvet)

    num4 = browser.find_element(By. CLASS_NAME, "form-control")
    num4.send_keys(otvet)

    num5 = browser.find_element(By. CLASS_NAME, "btn.btn-primary")
    num5.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()