from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display
from clint.textui import colored

def XssCheck(uri, xss, echo):
    result = None
    try:
        exploit = "".join((uri,xss))
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Firefox()
        driver.get(exploit)
        WebDriverWait(driver, 3).until(EC.alert_is_present(), "")
        result = exploit
        if echo:
            print("%s %s\n"%(colored.red("XSS found in URL: "), colored.green(exploit)))
    except TimeoutException:
        if echo:
            print("%s %s\n"%(colored.green("No XSS for URL: "), colored.blue(exploit)))
    driver.quit()
    display.stop()
    return result
