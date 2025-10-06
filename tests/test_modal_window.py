import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Test de la fenêtre modale")
@allure.description("Vérifie que la fenêtre modale s'ouvre, affiche le contenu, puis se ferme correctement.")
def test_modal_interaction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://formy-project.herokuapp.com/modal")

    # 1. Cliquer sur le bouton pour lancer la modal
    launch_button = driver.find_element(By.ID, "modal-button")
    launch_button.click()

    time.sleep(1)  # Attente pour que la modal s'affiche (à ajuster avec WebDriverWait si besoin)

    # 2. Vérifier que la modal est affichée
    modal_element = driver.find_element(By.CLASS_NAME, "modal-content")
    assert modal_element.is_displayed(), "La fenêtre modale ne s'est pas affichée."

    # 3. Vérifier le contenu de la modal (exemple : titre ou texte)
    modal_title = driver.find_element(By.CLASS_NAME, "modal-title")
    assert "Modal title" in modal_title.text, " Le titre de la modal est incorrect ou absent."

    # 4. Cliquer sur le bouton "Close" dans la modal
    close_button = driver.find_element(By.ID, "close-button")
    close_button.click()

    time.sleep(1)  # Attente pour que la modal se ferme

    # 5. Vérifier que la modal est bien fermée (pas visible)
    assert not modal_element.is_displayed(), " La fenêtre modale ne s'est pas fermée correctement."

    driver.quit()
