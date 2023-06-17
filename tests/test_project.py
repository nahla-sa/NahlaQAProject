from pages.home_page import HomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")
    home_page.is_products_located()
    home_page.add_products_to_cart()
    home_page.click_on_shopping_cart()
    home_page.is_your_cart_located()
    home_page.are_products_in_the_cart()
    home_page.click_on_checkout()
    home_page.is_checkout_your_information_located()
    home_page.fill_all_fields_on_checkout("Asya", "Aksu", "11000")
    home_page.is_checkout_overview_located()
    home_page.are_products_located_on_checkout_overview()
    home_page.click_on_finish()
    home_page.is_checkout_complete_located()
    home_page.click_on_menu()
    home_page.click_on_log_out()
    home_page.is_log_in_located()

    




