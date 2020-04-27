from django.core.exceptions import ImproperlyConfigured
from django_extensions.management.commands.show_urls import Command
from django.conf import settings
import importlib


def get_all_uris() -> list:
    """
    Responsible for extracting all the URIs registered via the ROOT_URLCONF in settings
    :return: ``list``
    """
    comm = Command()
    if not hasattr(settings, "ROOT_URLCONF"):
        raise ImproperlyConfigured("Settings doesn't containt ROOT_URLCONF")

    # import the actual module
    root_urls = importlib.import_module(getattr(settings, "ROOT_URLCONF"))

    return comm.extract_views_from_urlpatterns(root_urls.urlpatterns)
