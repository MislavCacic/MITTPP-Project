from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup():
    chromeOptions = Options()
    chromeOptions.add_argument("--start-fullscreen")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chromeOptions)
    driver.maximize_window()
    return driver

#Prijava korisnika
def testLogin(driver):
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    time.sleep(1)
    
    usernameField = driver.find_element(By.ID, "user-name")
    usernameField.send_keys("problem_user")
    time.sleep(1)

    passwordField = driver.find_element(By.ID, "password")
    passwordField.send_keys("secret_sauce")
    time.sleep(1)

    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    print("Login test passed!")

#Dodavanje prvog artikla u košaricu 
def testAddToCart(driver):
    time.sleep(1)

    addToCartButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(), 'Add to cart')])[1]"))
    )

    addToCartButton.click()
    time.sleep(1)

    print("Add to cart test passed!")

#Otvaranje košarice i provjera postoji li artikl u košarici
def testViewCart(driver):
    time.sleep(1)

    cartButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    )

    cartButton.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))

    print("View cart test passed!")

#Uklanjanje prvog artikla koji je u košarici
def testRemoveFromCart(driver):
    time.sleep(1)

    removeButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(), 'Remove')])[1]"))
    )

    removeButton.click()
    time.sleep(1)

    print("Remove from cart test passed!")

#Povratak na main/home page
def testReturnToHome(driver):
    time.sleep(2)

    continueShoppingButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "continue-shopping"))
    )
    
    continueShoppingButton.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

    print("Return to home test passed!")

#Odjava korisnika
def testLogout(driver):
    time.sleep(1)

    menuButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )

    menuButton.click()
    time.sleep(1)
    
    logoutButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )

    logoutButton.click()
    time.sleep(3)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))

    print("Logout test passed!")

if __name__ == "__main__":
    driver = setup()
    try:
        testLogin(driver)
        testAddToCart(driver)
        testViewCart(driver)
        testRemoveFromCart(driver)
        testReturnToHome(driver)
        testLogout(driver)
    finally:
        driver.quit()