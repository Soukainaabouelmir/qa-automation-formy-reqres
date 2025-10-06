import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@allure.title("Champ 'First name' obligatoire")
@allure.description("Teste que le formulaire affiche une erreur ou empêche la soumission si le champ 'First name' est vide.")
def test_first_name_required():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")

    # Champ First Name laissé vide volontairement
    # driver.find_element(By.ID, "first-name").send_keys("")

    # Remplir les autres champs
    driver.find_element(By.ID, "last-name").send_keys("Abouelmir")
    driver.find_element(By.ID, "job-title").send_keys("Web Developer")
    driver.find_element(By.ID, "radio-button-3").click()
    driver.find_element(By.ID, "checkbox-2").click()
    select = Select(driver.find_element(By.ID, "select-menu"))
    select.select_by_visible_text("0-1")
    driver.find_element(By.ID, "datepicker").send_keys("10/12/2025")

    # Cliquer sur le bouton Submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()

    time.sleep(1)  # Attendre la réponse du formulaire

    # Validation : le message de confirmation ne doit PAS apparaître
    assert "Thanks for submitting your form" not in driver.page_source, "Le formulaire a été soumis alors que 'First name' est vide"

    driver.quit()
