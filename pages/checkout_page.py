from playwright.sync_api import expect


class CheckoutPage:

    def __init__(self, page):

        self.page = page

        self.first_name = page.get_by_placeholder(
            "First Name"
        )

        self.last_name = page.get_by_placeholder(
            "Last Name"
        )

        self.postal_code = page.get_by_placeholder(
            "Zip/Postal Code"
        )

        self.continue_button = page.get_by_role(
            "button",
            name="Continue"
        )

        self.finish_button = page.get_by_role(
            "button",
            name="Finish"
        )

        self.order_confirmation = page.get_by_text(
            "Thank you for your order!"
        )

    def complete_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.first_name.fill(first_name)

        self.last_name.fill(last_name)

        self.postal_code.fill(postal_code)

        self.continue_button.click()

    def finish_order(self):

        self.finish_button.click()

    def validate_order_confirmation(self):

        expect(
            self.order_confirmation
        ).to_be_visible()