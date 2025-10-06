import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Test des cases à cocher pour le champ 'Genre'")
@allure.description("Vérifie que les cases à cocher 'Male', 'Female' et 'Prefer not to say' fonctionnent correctement (sélection multiple possible).")
def test_checkboxes_genre():
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")
    driver.maximize_window()

    # Localisation des checkboxes
    checkbox_male = driver.find_element(By.ID, "checkbox-1")
    checkbox_female = driver.find_element(By.ID, "checkbox-2")
    checkbox_prefer_not = driver.find_element(By.ID, "checkbox-3")

    # Coche chaque case
    checkbox_male.click()
    assert checkbox_male.is_selected(), "La case 'Male' n'est pas cochée."

    checkbox_female.click()
    assert checkbox_female.is_selected(), "La case 'Female' n'est pas cochée."

    checkbox_prefer_not.click()
    assert checkbox_prefer_not.is_selected(), "La case 'Prefer not to say' n'est pas cochée."

    # Décocher une case (Male)
    checkbox_male.click()
    assert not checkbox_male.is_selected(), "La case 'Male' devrait être décochée."

    # Optionnel : soumettre le formulaire
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    submit_button.click()

    time.sleep(2)  # Pause pour voir le résultat (peut être retirée pour tests CI)

    driver.quit()
