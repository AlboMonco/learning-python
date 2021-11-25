from selenium import webdriver
from selenium.webdriver.common.keys import Keys #/
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import os


def web(text:str):
    serv = Service(os.path.join("C:\\","Users","HP","Code","geckodriver.exe"))
    firefox = webdriver.Firefox(service=serv)
    firefox.get("https://www.google.com.br")
    path_button = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]"
    path_to_write = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    firefox.find_element(By.XPATH, path_to_write).send_keys(text)
    firefox.find_element(By.XPATH, path_button).click()

    firefox.quit()


if __name__ == "__main__":
    web("Bolo de atum")