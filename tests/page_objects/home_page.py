from playwright.sync_api import Page, expect
import os

class HomePage:
    TITLE = "Swag Labs"
    BURGER_MENU_BTN = 'button[id="react-burger-menu-btn"]'
    SORT_DROPDOWN = 'select[data-test="product_sort_container"]'

    PRODUCT_BACKPACK_LINK = 'a[id="item_4_title_link"]'
    PRODUCT_BIKE_LIGHT_LINK = 'a[id="item_0_title_link"]'
    PRODUCT_BOLT_TSHIRT_LINK = 'a[id="item_1_title_link"]'
    PRODUCT_FLEECE_JACKET_LINK = 'a[id="item_5_title_link"]'
    PRODUCT_ONESIE_LINK = 'a[id="item_2_title_link"]'
    PRODUCT_TEST_TSHIRT_LINK = 'a[id="item_3_title_link"]'

    ADD_BACKPACK_BTN = 'button[data-test="add-to-cart-sauce-labs-backpack"]'
    ADD_BIKE_LIGHT_BTN = 'button[data-test="add-to-cart-sauce-labs-bike-light"]'
    ADD_BOLT_TSHIRT_BTN = 'button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
    ADD_FLEECE_JACKET_BTN = 'button[data-test="add-to-cart-sauce-labs-fleece-jacket"]'
    ADD_ONESIE_BTN = 'button[data-test="add-to-cart-sauce-labs-onesie"]'
    ADD_TEST_TSHIRT_BTN = 'button[data-test="add-to-cart-test.allthethings-t-shirt-(red)"]'

    TWITTER_LINK = 'a[href="https://twitter.com/saucelabs"]'
    FACEBOOK_LINK = 'a[href="https://www.facebook.com/saucelabs"]'
    LINKEDIN_LINK = 'a[href="https://www.linkedin.com/company/sauce-labs/"]'

    TERMS_LINK = 'a[href*="terms"]'
    PRIVACY_LINK = 'a[href*="privacy"]'

    def __init__(self, page: Page):
        self.page = page
    
    def check_title(self):
        expect(self.page).to_have_title(self.TITLE)

    def open_burger_menu(self):
        self.page.click(self.BURGER_MENU_BTN)

    def sort_products(self, sort_value):
        self.page.select_option(self.SORT_DROPDOWN, sort_value)
        
    def open_product_backpack(self):
        self.page.click(self.PRODUCT_BACKPACK_LINK)

    def add_backpack_to_cart(self):
        self.page.click(self.ADD_BACKPACK_BTN)

    def add_bike_light_to_cart(self):
        self.page.click(self.ADD_BIKE_LIGHT_BTN)

    def add_bolt_tshirt_to_cart(self):
        self.page.click(self.ADD_BOLT_TSHIRT_BTN)

    def add_fleece_jacket_to_cart(self):
        self.page.click(self.ADD_FLEECE_JACKET_BTN)

    def add_onesie_to_cart(self):
        self.page.click(self.ADD_ONESIE_BTN)

    def add_test_tshirt_to_cart(self):
        self.page.click(self.ADD_TEST_TSHIRT_BTN)

    def open_twitter(self):
        self.page.click(self.TWITTER_LINK)

    def open_facebook(self):
        self.page.click(self.FACEBOOK_LINK)

    def open_linkedin(self):
        self.page.click(self.LINKEDIN_LINK)

    def open_terms(self):
        self.page.click(self.TERMS_LINK)

    def open_privacy(self):
        self.page.click(self.PRIVACY_LINK)