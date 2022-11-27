# sudo apt-get install gir1.2-appindicator3-0.1

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import time
import os

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")

from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator


# enter your login username
login_username = os.getenv("USERNAME")  # Change this
# enter your login password
login_password = "PASSWORD"  # Change this

###########################################################

# enter the element for username input field
element_for_username = "userId"
# enter the element for password input field
element_for_password = "password"
# enter the element for submit button
element_for_submit = "Submit22"

###########################################################

executable_path = os.path.abspath("chromedriver")
login_website_link = "http://www.gstatic.com/generate_204"
logout_website_link = "http://phc.prontonetworks.com/cgi-bin/authlogout"


###########################################################
def Connect(dummy=0):
    # chrome_options=options, executable_path=r"C:\chromedriver\chromedriver.exe", )

    # browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
    # browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path,
        chrome_options=chrome_options,
    )
    driver.get((login_website_link))

    try:
        username_element = driver.find_element(By.NAME, element_for_username)
        username_element.send_keys(login_username)
        password_element = driver.find_element(By.NAME, element_for_password)
        password_element.send_keys(login_password)
        signInButton = driver.find_element(By.NAME, element_for_submit)
        signInButton.click()
        #### to quit the browser uncomment the following lines ####
        time.sleep(1)
        driver.quit()
        time.sleep(1)
        # browserExe = "firefox"
        # os.system("pkill -f "+browserExe)
        # os.system("killall chrome")
        status = "Connected"
    except Exception:
        #### This exception occurs if the element are not found in the webpage.
        print("Some error occured :(")

        #### to quit the browser uncomment the following lines ####
        driver.quit()

        # browserExe = "firefox"
        # os.system("pkill -f "+browserExe)
        # os.system("killall chrome")
        status = "Not able to Connect"

    os.system(f"""notify-send "Wifi" "{status}" """)


###########################################################
def Disconnect(dummy=0):
    # chrome_options=options, executable_path=r"C:\chromedriver\chromedriver.exe", )

    # browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
    # browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path,
        chrome_options=chrome_options,
    )
    # uncomment this line,for chrome users
    driver.get((logout_website_link))

    time.sleep(1)
    driver.quit()
    time.sleep(1)
    # os.system("killall chrome")

    os.system(f"""notify-send "Wifi" "Disconnected" """)


if __name__ == "__main__":
    ind = appindicator.Indicator.new(
        "VIT Tools",
        os.path.abspath("images" + os.sep + "vit_logo.jpeg"),
        appindicator.IndicatorCategory.SYSTEM_SERVICES,
    )
    ind.set_status(appindicator.IndicatorStatus.ACTIVE)
    ind.set_attention_icon("indicator-messages-new")

    # create a menu
    menu = Gtk.Menu()

    buf1 = "Connect Wifi"
    buf2 = "Disconnect Wifi"

    menu_items = Gtk.MenuItem(buf1)
    menu.append(menu_items)
    menu_items.connect("activate", Connect)
    menu_items.show()

    menu_items = Gtk.MenuItem(buf2)
    menu.append(menu_items)
    menu_items.connect("activate", Disconnect)
    menu_items.show()

    ind.set_menu(menu)

    Gtk.main()
