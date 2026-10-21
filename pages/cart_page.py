from playwright.sync_api import expect


class CartPage:

    def __init__(self, page):

        self.page = page

        self.backpack = page.get_by_text(
            "Sauce Labs Backpack"
        )

        self.checkout_button = page.get_by_role(
            "button",
            name="Checkout"
        )

    def validate_backpack(self):

        expect(
            self.backpack
        ).to_be_visible()

    def start_checkout(self):

        self.checkout_button.click()
