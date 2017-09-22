from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display
from clint.textui import colored

def XssCheck(z):
    try:
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Firefox()
        driver.get(z)
        WebDriverWait(driver, 3).until(EC.alert_is_present(), "")
        print colored.red("XSS found in URL: ") + colored.green(z)
        with open('vulnerable.txt', 'a') as outfile:
            result_line = outfile.writelines(z + "\n")
    except TimeoutException:
        print colored.green("No XSS for URL: ") + colored.blue(z)
    driver.quit()
    display.stop()
    return