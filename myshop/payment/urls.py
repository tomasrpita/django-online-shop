from django.urls import path
from . import views, webhooks
from django.utils.translation import gettext_lazy as _

app_name = "payment"
# Traslated URL patterns will include a language prefix because they are included under i18n_patterns() in the main urls.py
urlpatterns = [
    path(_("process/"), views.payment_process, name="process"),
    path(_("completed/"), views.payment_completed, name="completed"),
    path(_("canceled/"), views.payment_canceled, name="canceled"),
    # path("webhook/", webhooks.stripe_webhook, name="stripe-webhook"),
]
