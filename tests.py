
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


email = "test111111eq413r.john@gmail.com"

PATH = r"C:\Users\Daniel\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Inicializácia prehliadača
driver = webdriver.Chrome(PATH)

# Navigácia na webovú stránku
driver.get("http://localhost:3000/")
time.sleep(10)

# Checking tab name
driver.find_element(By.XPATH, "//title[contains(text(),'Tdrive')]")

# Checking presence of login form elements
driver.find_element(By.XPATH, "//div[@class='title'][contains(text(),'Sign in to Tdrive')]")
driver.find_element(By.XPATH, "//div[@class='subtitle'][contains(text(),'Happy to see you')]")
driver.find_element(By.XPATH, "//input[@id='username']").is_displayed()
driver.find_element(By.XPATH, "//input[@id='password']")
driver.find_element(By.XPATH, "//button[@id='login_btn']")
driver.find_element(By.XPATH, "//a[@id='create_btn']")


# Checking functionality of create button
driver.find_element(By.XPATH," //a[@id='create_btn']").click()
time.sleep(5)

# Checking presence of create form elements
driver.find_element(By.XPATH, "//input[@id='first_name_create']")
driver.find_element(By.XPATH, "//input[@id='last_name_create']")
driver.find_element(By.XPATH, "//input[@id='email_create']")
driver.find_element(By.XPATH, "//input[@id='password_create']")
driver.find_element(By.XPATH, "//button[@id='continue_btn']")

# Creating account
driver.find_element(By.XPATH, "//input[@id='first_name_create']").send_keys("Tester")
driver.find_element(By.XPATH, "//input[@id='last_name_create']").send_keys("John")
driver.find_element(By.XPATH, "//input[@id='email_create']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='password_create']").send_keys("12345678")

# Checking functionality of create button
driver.find_element(By.XPATH, "//button[@id='continue_btn']").click()
time.sleep(15)

# Log out
driver.find_element(By.XPATH, "//span[contains(text(),'@gmail.com')][1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[contains(text(),'Sign out')]").click()
time.sleep(10)

# Log in
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(email)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("12345678")
driver.find_element(By.XPATH, "//button[@id='login_btn']").click()
time.sleep(10)

# Create modal
driver.find_element(By.XPATH, "//button[2]").click()
driver.find_element(By.XPATH, "//span[contains(text(),'Create a folder')]")
driver.find_element(By.XPATH, "//span[contains(text(),'Create a link file')]")
driver.find_element(By.XPATH, "//span[contains(text(),'ONLYOFFICE Word Document')]")
driver.find_element(By.XPATH, "//span[contains(text(),'ONLYOFFICE Excel Document')]")
driver.find_element(By.XPATH, "//span[contains(text(),'ONLYOFFICE PowerPoint Document')]")
driver.find_element(By.XPATH, "//div[@class='absolute top-0 right-0 pt-4 pr-4']").click()

# Change language
driver.find_element(By.XPATH, "//span[contains(text(),'@gmail.com')][1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[contains(text(),'Account settings')]").click()
driver.find_element(By.XPATH, "//select").click()
dropdown = driver.find_element(By.XPATH, "//select")
select = Select(dropdown)
select.select_by_visible_text("Русский")
time.sleep(15)









# Interakcia s nájdeným elementom
# username_input.send_keys("MôjUžívateľskýNázov")
#
# # Hľadanie ďalšieho elementu pomocou XPath
# password_xpath = "//input[@id='password']"
# password_input = driver.find_element(By.XPATH, password_xpath)
#
# # Interakcia s ďalším elementom
# password_input.send_keys("MôjHeslo")
#
# # Kliknutie na tlačidlo pomocou XPath
# login_button_xpath = "//button[@id='loginButton']"
# login_button = driver.find_element(By.XPATH, login_button_xpath)
# login_button.click()

# Ukončenie testu
driver.quit()