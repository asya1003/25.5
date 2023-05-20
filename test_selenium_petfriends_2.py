import time
import pytest
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\Chromedriver\chromedriver_win32\chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID,'email').send_keys('asya3@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   header_text = pytest.driver.find_element(By.TAG_NAME,'h1').text
   assert  header_text == "PetFriends"

   #неявные ожидания
   driver.implicitly_wait(10)
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   driver.implicitly_wait(10)
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
   
   for i in range(len(names)):
      assert images[i].get_attribute('src') != '' or images[i].get_attribute('src') == ''
      assert names[i].text != '' or names[i].text == ''
      assert descriptions[i].text != '' or descriptions[i].text == ''
      #assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      driver.implicitly_wait(5)
      age = parts[1]
      #assert len(parts[0]) > 0
      #assert len(parts[1]) > 0'''

   pytest.driver.find_element(By.LINK_TEXT, 'Мои питомцы').click()
   statistic2 = pytest.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]')
   #time.sleep(5)
   parts = statistic2.text.split("\n")
   parts2 = parts[1].split(': ')

   '''# явные ожидания
   wait = WebDriverWait(driver, 10)
   element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-outline-success")))

   wait = WebDriverWait(driver, 10)
   wait.until(EC.presence_of_elements_located(By.TAG_NAME, 'tr'))'''

   pets_amount = pytest.driver.find_elements(By.TAG_NAME, "tr")

   assert parts2[1] == str(len(pets_amount)-1)

   photo = pytest.driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr > th > img")

   count_photo = 0
   count_not_photo = 0
   for i in range(len(photo)):
        if photo[i].get_attribute('src') != '':
            count_photo = count_photo + 1
        else:
            count_not_photo = count_not_photo + 1
   assert count_photo >= int(parts2[1])/2




