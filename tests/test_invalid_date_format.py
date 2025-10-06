import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@allure.title("Test du champ Date avec un format invalide")
@allure.description("Vérifie que le champ Date ne permet pas la soumission avec un format invalide (YYYY-MM-DD).")
def test_invalid_date_format():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://formy-project.herokuapp.com/form")

    # Renseigner un format invalide dans le champ date
    date_field = driver.find_element(By.ID, "datepicker")
    date_field.clear()
    date_field.send_keys("2025-10-12")  # Format ISO (invalide pour ce champ)
    date_field.send_keys(Keys.TAB)  # Sortir du champ pour déclencher validation

    # Soumettre le formulaire
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    submit_button.click()

    # Pause pour observation ou analyse
    time.sleep(2)

    # Récupérer la valeur du champ après soumission
    value = date_field.get_attribute("value")

    # Assertion simple : le champ ne doit pas accepter le format ISO
    assert value != "2025-10-12", "Le champ a accepté un format de date invalide (YYYY-MM-DD)."

    driver.quit()
