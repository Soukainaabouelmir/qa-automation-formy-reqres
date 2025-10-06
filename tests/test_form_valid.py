import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Définition du test avec un titre et une description pour Allure
@allure.title("Soumission du formulaire avec données valides")
@allure.description("Teste la soumission correcte du formulaire sur Formy Project avec des données valides.")
def test_form_submission():
    # Initialisation du navigateur Chrome
    driver = webdriver.Chrome()
    
    # Ouverture de la page du formulaire
    driver.get("https://formy-project.herokuapp.com/form")

    # Remplissage du champ "First name" avec la valeur "Soukaina"
    driver.find_element(By.ID, "first-name").send_keys("Soukaina")
    
    # Remplissage du champ "Last name" avec la valeur "Abouelmir"
    driver.find_element(By.ID, "last-name").send_keys("Abouelmir")
    
    # Remplissage du champ "Job title" avec la valeur "Web Developer"
    driver.find_element(By.ID, "job-title").send_keys("Web Developer")
    
    # Sélection du bouton radio avec l'ID "radio-button-3" (par exemple, "Female")
    driver.find_element(By.ID, "radio-button-3").click()
    
    # Coche de la case à cocher avec l'ID "checkbox-2" (par exemple, "College")
    driver.find_element(By.ID, "checkbox-2").click()
    
    # Sélection dans la liste déroulante "Years of experience" de l'option "0-1"
    select = Select(driver.find_element(By.ID, "select-menu"))
    select.select_by_visible_text("0-1")
    
    # Remplissage du champ date avec la date "10/12/2025"
    driver.find_element(By.ID, "datepicker").send_keys("10/12/2025")

    # Clic sur le bouton de soumission du formulaire (bouton avec classes CSS .btn.btn-lg.btn-primary)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()

    # Pause de 1 seconde pour laisser le temps à la page de charger la réponse
    time.sleep(1)
    
    # Vérification que la confirmation "Thanks for submitting your form" apparaît dans la page
    assert "Thanks for submitting your form" in driver.page_source
    
    # Fermeture du navigateur
    driver.quit()
