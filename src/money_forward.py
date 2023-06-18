from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_binary

import config


class MoneyForward:
  
  def __init__(self, email, password):
    self.email = email
    self.password = password

  def login(self):
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(3)
    
    driver.get('https://attendance.moneyforward.com/my_page')

    el = driver.find_element(By.CSS_SELECTOR, ".attendance-button-mfid.attendance-button-link.attendance-button-size-wide")
    el.click()

    el = driver.find_element(By.NAME, "mfid_user[email]")
    el.send_keys(self.email)

    el = driver.find_element(By.CSS_SELECTOR, ".LjJ8E2j_.submitBtn._AUBUrBM.bizDomain")
    el.click()

    el = driver.find_element(By.NAME, "mfid_user[password]")
    el.send_keys(self.password)

    el = driver.find_element(By.CSS_SELECTOR, ".LjJ8E2j_.submitBtn._AUBUrBM.bizDomain")
    el.click()

    return driver

  def clock_in(self):
    driver = self.login()

    el = driver.find_element(By.CLASS_NAME, "clock_in")
    el = el.find_element(By.TAG_NAME, "button")
    el.click()

  def clock_out(self):
    driver = self.login()

    el = driver.find_element(By.CLASS_NAME, "clock_out")
    el = el.find_element(By.TAG_NAME, "button")
    el.click()
  



