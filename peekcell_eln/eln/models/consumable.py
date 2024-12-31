from django.db import models
from django.utils.timezone import now

from eln.models.choices.product_status import ProductStatus


class Consumable(models.Model):
    status = models.CharField(
        max_length=8,
        choices=ProductStatus.choices,
        default=ProductStatus.RECEIVED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


    def open(self):
        if self.status == ProductStatus.OPENED:
            return
        if self.status == ProductStatus.CLOSED:
            raise ValueError('Product is already closed')
        self.status = ProductStatus.OPENED
        self.opened_at = now()
        self.save()

    def close(self):
        if self.status == ProductStatus.CLOSED:
            return
        if self.status == ProductStatus.RECEIVED:
            raise ValueError('Product was not opened')
        self.status = ProductStatus.CLOSED
        self.finished_at = now()
        self.save()
