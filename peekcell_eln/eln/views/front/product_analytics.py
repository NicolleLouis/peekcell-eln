from django.views.generic import ListView
import django_tables2 as tables
from django_tables2 import SingleTableMixin
import requests
from django.conf import settings


class ProductAnalyticTable(tables.Table):
    product_label = tables.Column(verbose_name="Product Label")
    has_one_opened = tables.BooleanColumn(verbose_name="Currently Opened")
    number_in_stock = tables.Column(verbose_name="Number in Stock")

    @staticmethod
    def get_row_attribute(record):
        if record["has_one_opened"] and record["number_in_stock"] == 0:
            return "table-warning"
        elif record["number_in_stock"] == 0:
            return "table-danger"
        return "table-success"

    class Meta:
        template_name = "django_tables2/bootstrap5.html"
        row_attrs = {
            "class": lambda record: ProductAnalyticTable.get_row_attribute(record)
        }

class ProductAnalyticsView(SingleTableMixin, ListView):
    table_class = ProductAnalyticTable
    template_name = "product_analytics.html"

    def get_queryset(self):
        url = f"{settings.BASE_URL}/api/product-analytics"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to fetch data from the product API")

        analytics = response.json()
        return analytics
