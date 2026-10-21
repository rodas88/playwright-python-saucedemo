from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):

        self.page = page

        # ==========================
        # LOCATOR USERNAME
        # ==========================

        self.username = page.get_by_role(
            "textbox",
            name="Username"
        )

        # ==========================
        # LOCATOR PASSWORD
        # ==========================

        self.password = page.get_by_role(
            "textbox",
            name="Password"
        )

        # ==========================
        # LOCATOR LOGIN BUTTON
        # ==========================

        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

        # ==========================
        # LOCATOR ERROR MESSAGE
        # ==========================

        self.error_message = page.locator(
            "[data-test='error']"
        )

    # ==========================
    # LOGIN
    # ==========================

    def login(
        self,
        username,
        password
    ):

        self.username.fill(
            username
        )

        self.password.fill(
            password
        )

        self.login_button.click()

    # ==========================
    # VALIDAR ERROR
    # ==========================

    def validate_login_error(self):

        expect(
            self.error_message
        ).to_be_visible()

        expect(
            self.error_message
        ).to_contain_text(
            "Username and password do not match"
        )