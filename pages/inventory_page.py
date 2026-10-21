class InventoryPage:

    def __init__(self, page):

        self.page = page

        self.add_backpack_button = page.get_by_role(
            "button",
            name="Add to cart"
        ).first

        self.shopping_cart = page.locator(
            ".shopping_cart_link"
        )

    def add_backpack_to_cart(self):

        self.add_backpack_button.click()

    def open_cart(self):

        self.shopping_cart.click()