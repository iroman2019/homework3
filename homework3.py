import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/")

def create_location(name, coords):
    driver.find_element(By.ID, "create-location-link").click()
    driver.find_element(By.ID, "location-name").send_keys(name)
    driver.find_element(By.ID, "location-coords").send_keys(coords)
    driver.find_element(By.XPATH, "//input[@value='Create location']").click()

create_location("Ki-falva", "23.012,13.021")

def wait_for_created_message():
    WebDriverWait(driver, 100).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"),
                                                          "Location has created"))
    print(driver.find_element(By.ID, "message-div"))

def appear_location_name(name):
    driver.get("http://www.learnwebservices.com/locations/?size=100")
    WebDriverWait(driver, 100).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//tr[td[text()='"+name+"']]"),
                                                          name))
    new_name = driver.find_element(By.XPATH, "//tr[td[text()='"+name+"']]/td[2]").text
    print(new_name)

def wait_for_appier(name):
    name2 = name + str(time.time())
    create_location(name2, "1,1")
    appear_location_name(name2)
    return name2

def modify_location(name, modified_name):
    driver.find_element(By.XPATH, "//tr[td[text()='"+name+"']]/td[last()]/button[text()='Edit']").click()
    driver.find_element(By.ID, "update-location-name").clear()
    new_modified_name = modified_name+str(time.time())
    driver.find_element(By.ID, "update-location-name").send_keys(new_modified_name)
    driver.find_element(By.XPATH, "//input[@value='Update location']").click()
    return new_modified_name

def wait_for_modified_message():
    WebDriverWait(driver, 100).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"),
                                                          "Location has modified"))
    print(driver.find_element(By.ID, "message-div"))


def wait_for_message(message):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "message-div"),
                                                          message))
    message_text = driver.find_element(By.ID, "message-div").text
    print(message_text)

# Módosítás tesztesete
def modify_test(name, modified_name):
    driver.get("http://www.learnwebservices.com/locations/?size=100")
    name2 = wait_for_appier(name)
    new_name = modify_location(name2, modified_name)
    print("New name is: "+new_name)
    wait_for_modified_message()
    appear_location_name(new_name)


#river.get("http://www.learnwebservices.com/locations/?size=100")
#create_location("Piripócs", "1.12,1.1")
#appear_location_name("Piripócs")
#wait_for_appier("Bla-bla-city")

modify_test("Teszt_City", "Modified_City")