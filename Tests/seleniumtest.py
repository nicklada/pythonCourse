#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Создание экземпляра WebDriver
driver = webdriver.Chrome()

# Загрузка веб-страницы
driver.get("https://www.example.com")

# Взаимодействие с элементами страницы
element = driver.find_element_by_id("my_element")
element.send_keys("Hello, World!")
element.send_keys(Keys.RETURN)

# Извлечение информации со страницы
result = driver.find_element_by_xpath("//div[@id='result']")
print(result.text)

# Закрытие браузера
driver.quit()