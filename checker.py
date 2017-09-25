from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display
from clint.textui import colored

def GetFirefoxProfile(useProxy, proxyHost, proxyPort):
    profile = webdriver.FirefoxProfile()
    if useProxy:
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", proxyHost)
        profile.set_preference("network.proxy.http_port", proxyPort)
        profile.set_preference("network.proxy.ssl", proxyHost)
        profile.set_preference("network.proxy.ssl_port", proxyPort)
        profile.update_preferences()
    return profile
def XssCheck(exploit, echo, useProxy, proxyHost, proxyPort, outFileName):
    try:
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Firefox(firefox_profile=GetFirefoxProfile(useProxy,proxyHost,proxyPort))
        driver.get(exploit)
        WebDriverWait(driver, 3).until(EC.alert_is_present(), "")
        if echo:
            print("%s %s"%(colored.green("XSS found in URL: "), colored.white(exploit)))
        with open(outFileName, 'a') as outfile:
            outfile.writelines("%s\n"%(exploit))
            outfile.close()
    except TimeoutException:
        if echo:
            print("%s %s"%(colored.blue("No XSS for URL: "), colored.white(exploit)))
    try:
        driver.quit()
    except WebDriverException:
        pass
    display.stop()

