from eln.models import Product


class ProductAnalytics:
    def __init__(self, product_name: str, product_label: str):
        self.product_label = product_label
        self.products = self.get_products(product_name)
        self.has_one_opened = self.has_one_opened()
        self.number_in_stock = self.get_number_in_stock()

    @staticmethod
    def get_products(product_name):
        return Product.objects.filter(name=product_name)

    def has_one_opened(self):
        return self.products.filter(status='opened').count() >= 1

    def get_number_in_stock(self):
        return self.products.filter(status='received').count()
