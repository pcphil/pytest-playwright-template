from playwright.sync_api import Page, Locator
import os

class LoginPage:
    """Page Object for https://www.saucedemo.com/"""

    # Locators
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"
    LOGIN_FORM = ".login_wrapper"

    def __init__(self, page: Page):
        """Initialize LoginPage with a Playwright page instance."""
        self.page = page

    def navigate(self) -> None:
        """Navigate to the Sauce Demo login page."""
        self.page.goto("https://www.saucedemo.com/")

    def fill_username(self, username: str =os.getenv("TEST_USER_EMAIL")) -> None:
        """Fill the username field.
        
        Args:
            username: Username string to enter
        """
        self.page.locator(self.USERNAME_INPUT).fill(username)

    def fill_password(self, password: str =os.getenv("TEST_USER_PASSWORD")) -> None:
        """Fill the password field.
        
        Args:
            password: Password string to enter
        """
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_login(self) -> None:
        """Click the login button."""
        self.page.locator(self.LOGIN_BUTTON).click()
        # Wait for navigation or error message to appear
        self.page.wait_for_load_state("networkidle")

    def login(self, username: str, password: str) -> None:
        """Perform login action.
        
        Args:
            username: Username to login with
            password: Password to login with
        """
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Get the error message text if present.
        
        Returns:
            Error message text, or empty string if not visible
        """
        error_locator = self.page.locator(self.ERROR_MESSAGE)
        if error_locator.is_visible():
            return error_locator.text_content() or ""
        return ""

    def is_error_displayed(self) -> bool:
        """Check if error message is displayed.
        
        Returns:
            True if error is visible, False otherwise
        """
        return self.page.locator(self.ERROR_MESSAGE).is_visible()

    def is_login_form_visible(self) -> bool:
        """Check if login form is visible on the page.
        
        Returns:
            True if login form is visible, False otherwise
        """
        return self.page.locator(self.LOGIN_FORM).is_visible()

    def get_page_title(self) -> str:
        """Get the page title.
        
        Returns:
            Page title string
        """
        return self.page.title()
