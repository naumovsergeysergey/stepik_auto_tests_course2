from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    #открытие страницы
    browser.get(link)

    #считаем значение в задании
    num1 = browser.find_element(By.ID, "input_value")
    x = num1.text
    print(x)
    num2 = calc(x)
    print(num2)

    time.sleep(5)
    #проскролить страницу на 100 пикселей
    submit = browser.find_element(By.CLASS_NAME, "form-check-label")
    # browser.execute_script("window.scrollBy(0,100);")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)


    time.sleep(5)
    #находим поле для ввода и ввести значение в текстовое поле
    num3 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    num3.send_keys(num2)

    #отмечаем чекбокс 1 и 2
    num4 = browser.find_element(By.ID, 'robotCheckbox')
    num4.click()
    num5 = browser.find_element(By.ID, 'robotsRule')
    num5.click()

    #нажимаем кнопку которую нашли ранее
    submit = browser.find_element(By.TAG_NAME, "button")
    time.sleep(5)
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
