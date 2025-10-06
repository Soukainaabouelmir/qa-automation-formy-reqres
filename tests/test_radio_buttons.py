import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Test des boutons radio pour le champ 'Sex'")
@allure.description("Vérifie que les boutons radio pour le champ 'Sex' fonctionnent correctement (sélection unique).")
def test_radio_buttons_high_school():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")

    # Sélectionner "High School"
    radio_high_school = driver.find_element(By.ID, "radio-button-1")
    radio_high_school.click()
    assert radio_high_school.is_selected(), "Le bouton radio 'High School' n'est pas sélectionné."

    # Sélectionner "College"
    radio_college = driver.find_element(By.ID, "radio-button-2")
    radio_college.click()
    assert radio_college.is_selected(), "Le bouton radio 'College' n'est pas sélectionné."
    assert not radio_high_school.is_selected(), "Le bouton 'High School' devrait être désélectionné après avoir sélectionné 'College'."

    # Sélectionner "Grad School"
    radio_none = driver.find_element(By.ID, "radio-button-3")
    radio_none.click()
    assert radio_none.is_selected(), "Le bouton 'Grad School' n'est pas sélectionné."
    assert not radio_college.is_selected(), "Le bouton 'College' devrait être désélectionné après avoir sélectionné 'Grad School'."

    driver.quit()
