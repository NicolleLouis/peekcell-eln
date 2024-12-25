from django.db import models


class ProductStatus(models.TextChoices):
    """
    Product statuses
    """
    RECEIVED = 'received', 'Received'
    OPENED = 'opened', 'Opened'
    CLOSED = 'closed', 'Closed'
