from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())
action = ActionChains(driver)
driver.get("http://opensource-demo.orangehrmlive.com/")

sleep(1)

driver.find_element(By.NAME,value="username").send_keys("Admin")
driver.find_element(By.NAME,value="password").send_keys("admin123")
driver.find_element(By.XPATH,value="//button[@type='submit']").click()

driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()

sleep(2)
driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input").send_keys("keerthi")
driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input").send_keys("priya")

driver.find_element(By.XPATH,value="//button[@type='submit']").click()


driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
sleep(2)
driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
sleep(2)
role = driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
action.click(role).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ENTER).perform()
sleep(2)
status = driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div")
action.click(status).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ENTER).perform()
sleep(2)

driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("keerthi priya")
driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("keerthi")
driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Keerthi@123")
driver.find_element(By.XPATH,value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Keerthi@123")

driver.find_element(By.XPATH,value="//button[@type='submit']").click()

