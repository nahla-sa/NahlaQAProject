from selenium.webdriver.common.by import By  
import time  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.support.select import Select  
from selenium.webdriver.common.action_chains import ActionChains  


class HomePage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()  

    def login(self, username, password):
        username_field_locator = (By.ID, "user-name")  
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))  
        wait_username_field.click()  
        wait_username_field.clear()  
        wait_username_field.send_keys(username)  

        password_field = self.selenium_driver.find_element(By.ID, "password")  
        password_field.click()  
        password_field.clear()  
        password_field.send_keys(password)  

        login_button = self.selenium_driver.find_element(By.XPATH, "//input[@id=\"login-button\"]")  
        login_button.click()  


    def is_products_located(self):
        products_locator = (By.XPATH, "//span[@class=\"title\" and text()=\"Products\"]")  
        wait_products_field = self.wait.until(EC.presence_of_element_located(products_locator))
        products_field_text = wait_products_field.text
        assert products_field_text == "Products"

    def add_products_to_cart(self):
        sauce_labs_backpack_locator = (By.XPATH, "//div[text()=\"Sauce Labs Backpack\"]")  
        wait_sauce_labs_backpack_field = self.wait.until(EC.element_to_be_clickable(sauce_labs_backpack_locator))
        
        button_add_to_card_backpack_field = self.selenium_driver.find_element(By.XPATH, "//button[@id=\"add-to-cart-sauce-labs-backpack\"]")
        button_add_to_card_backpack_field.click()
        
        sauce_labs_bike_light_locator = (By.XPATH, "//div[text()=\"Sauce Labs Bike Light\"]")  
        wait_sauce_labs_light_field = self.wait.until(EC.element_to_be_clickable(sauce_labs_bike_light_locator))
        
        button_add_to_card_light_field = self.selenium_driver.find_element(By.XPATH, "//button[@id=\"add-to-cart-sauce-labs-bike-light\"]")
        button_add_to_card_light_field.click()


    def click_on_shopping_cart(self):
        shoping_cart_locator = (By.CSS_SELECTOR, "a.shopping_cart_link")
        wait_shopping_cart = self.wait.until(EC.element_to_be_clickable(shoping_cart_locator))
        wait_shopping_cart.click()

    def is_your_cart_located(self):
        your_cart_locator = (By.XPATH, "//span[@class=\"title\" and text()=\"Your Cart\"]")
        wait_your_cart_field = self.wait.until(EC.presence_of_element_located(your_cart_locator))
        your_cart_field_text = wait_your_cart_field.text
        assert your_cart_field_text == "Your Cart"


    def are_products_in_the_cart(self):
        first_product = self.selenium_driver.find_element(By.XPATH, "//div[@class=\"inventory_item_name\" and text()=\"Sauce Labs Backpack\"]")
        first_product_text = first_product.text

        backack_text = "Sauce Labs Backpack"

        second_product = self.selenium_driver.find_element(By.XPATH, "//div[@class=\"inventory_item_name\" and text()=\"Sauce Labs Bike Light\"]")
        second_product_text = second_product.text

        bike_light_text = "Sauce Labs Bike Light"

        assert (first_product_text, second_product_text) == (backack_text, bike_light_text)

    
    def click_on_checkout(self):
        checkout_locator = (By.XPATH,"//button[@id=\"checkout\"]")
        wait_checkout_field = self.wait.until(EC.element_to_be_clickable(checkout_locator))
        wait_checkout_field.click()

    def is_checkout_your_information_located(self):
        checkout_your_information_locator = (By.XPATH, "//span[@class=\"title\" and text()=\"Checkout: Your Information\"]")
        wait_checkout_your_information_field = self.wait.until(EC.presence_of_element_located(checkout_your_information_locator))
        checkout_your_information_text = wait_checkout_your_information_field.text
        assert checkout_your_information_text == "Checkout: Your Information"

    def fill_all_fields_on_checkout(self, first_name, last_name, zip_code):
        first_name_field_locator = (By.ID, "first-name")  
        wait_first_name_field = self.wait.until(EC.element_to_be_clickable(first_name_field_locator))  
        wait_first_name_field.click()  
        wait_first_name_field.clear()  
        wait_first_name_field.send_keys(first_name)  

        last_name_field = self.selenium_driver.find_element(By.ID, "last-name")  
        last_name_field.click()  
        last_name_field.clear()  
        last_name_field.send_keys(last_name)

        zip_code_field = self.selenium_driver.find_element(By.ID, "postal-code")  
        zip_code_field.click()  
        zip_code_field.clear()  
        zip_code_field.send_keys(zip_code)    

        continue_button = self.selenium_driver.find_element(By.XPATH, "//input[@id=\"continue\"]")  
        continue_button.click()  

    def is_checkout_overview_located(self):
        checkout_overview_locator = (By.XPATH, "//span[@class=\"title\" and text()=\"Checkout: Overview\"]")
        wait_checkout_overview_field = self.wait.until(EC.presence_of_element_located(checkout_overview_locator))
        checkout_overview_field_text = wait_checkout_overview_field.text
        assert checkout_overview_field_text == "Checkout: Overview"


    def are_products_located_on_checkout_overview(self):
        product_1_field = self.selenium_driver.find_element(By.XPATH, "//div[@class=\"inventory_item_name\" and text()=\"Sauce Labs Backpack\"]")
        product_1_text = product_1_field.text

        backack_text = "Sauce Labs Backpack"

        product_2_field = self.selenium_driver.find_element(By.XPATH, "//div[@class=\"inventory_item_name\" and text()=\"Sauce Labs Bike Light\"]")
        product_2_text = product_2_field.text

        bike_light_text = "Sauce Labs Bike Light"

        assert (product_1_text, product_2_text) == (backack_text, bike_light_text)

    
    def click_on_finish(self):
        finish_locator = (By.XPATH,"//button[@id=\"finish\"]")
        finish_button = self.wait.until(EC.element_to_be_clickable(finish_locator))
        finish_button.click()

    def is_checkout_complete_located(self):
        checkout_complete_locator = (By.XPATH, "//span[@class=\"title\" and text()=\"Checkout: Complete!\"]")
        checkout_complete_field = self.wait.until(EC.presence_of_element_located(checkout_complete_locator))
        checkout_complete_field_text = checkout_complete_field.text
        assert checkout_complete_field_text == "Checkout: Complete!"

    def click_on_menu(self):
        menu_locator = (By.XPATH,"//button[@id=\"react-burger-menu-btn\"]")
        menu_button = self.wait.until(EC.element_to_be_clickable(menu_locator))
        menu_button.click()

    def click_on_log_out(self):

        all_items_locator = (By.XPATH, "//a[@id=\"inventory_sidebar_link\"]")
        wait_all_items = self.wait.until(EC.element_to_be_clickable(all_items_locator))

        find_element_about = self.selenium_driver.find_element(By.XPATH, "//a[@id=\"about_sidebar_link\"]")

        find_element_log_out = self.selenium_driver.find_element(By.XPATH,"//a[@id=\"logout_sidebar_link\"]")

        find_element_reset_app_state = self.selenium_driver.find_element(By.XPATH,"//a[@id=\"reset_sidebar_link\"]")
        

        find_element_log_out.click()


    def is_log_in_located(self):

        checkout_complete_locator = (By.XPATH, "//span[@class=\"title\" and text()=\"Checkout: Complete!\"]")
        wait_to_disappear_checkout_complete = self.wait.until(EC.invisibility_of_element_located(checkout_complete_locator))

        menu_locator = (By.XPATH,"//button[@id=\"react-burger-menu-btn\"]")
        wait_to_disappear_menu = self.wait.until(EC.invisibility_of_element_located(menu_locator))

        username_field_locator = (By.ID, "user-name") 
        username_wait = self.wait.until(EC.visibility_of_element_located(username_field_locator))

        password_field_locator = (By.ID, "password")
        password_wait = self.wait.until(EC.visibility_of_element_located(password_field_locator))




    


        


    

    


        

        


    

    

    




    

    





    
    
   
    


