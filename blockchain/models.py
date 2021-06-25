from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# For search by address logging.
class SearchAddress(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=50)
    valid = models.BooleanField(default=True)


# For search by transaction logging.
class SearchTransaction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    transaction = models.CharField(max_length=64)


class UserAddresses(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=50)


class UserOrders(models.Model):
    class OrderState(models.TextChoices):
        CREATED = 'CREATED', _('Created')
        COMPLETE = 'COMPLETE', _('Complete')

    class TransitionError(Exception):
        def __init__(self, message):
            self.message = message

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    address = models.ForeignKey(
        UserAddresses,
        on_delete=models.CASCADE, # TODO figure out correct cascades
    )
    state = models.CharField(max_length=20, choices=OrderState.choices, default=OrderState.CREATED)
    input_amount = models.DecimalField(max_digits=64, decimal_places=18)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def complete(self):
        if self.state == UserOrders.OrderState.CREATED:
            self.state = UserOrders.OrderState.COMPLETE
        else:
            raise UserOrders.TransitionError(message="Can only complete orders in created state")
