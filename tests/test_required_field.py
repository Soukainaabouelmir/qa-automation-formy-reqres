import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@allure.title("Champ 'First name' obligatoire")
@allure.description("Ce test illustre que le formulaire est soumis même si le champ 'First name' est vide, révélant l'absence de validation.")
def test_first_name_required():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")

    # Laisser 'First name' vide
    driver.find_element(By.ID, "last-name").send_keys("Abouelmir")
    driver.find_element(By.ID, "job-title").send_keys("Web Developer")
    driver.find_element(By.ID, "radio-button-3").click()
    driver.find_element(By.ID, "checkbox-2").click()
    Select(driver.find_element(By.ID, "select-menu")).select_by_visible_text("0-1")
    driver.find_element(By.ID, "datepicker").send_keys("10/12/2025")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()

    time.sleep(1)

    assert "Thanks for submitting your form" in driver.page_source, \
        "Le formulaire n'a pas été soumis — ce qui serait anormal pour ce site."

    # Astuce : mentionner dans Allure que le test révèle un manque de validation
    allure.attach("Aucune validation côté client détectée", name="Observation", attachment_type=allure.attachment_type.TEXT)

    driver.quit()
