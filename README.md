# Django Associations

## Description
A tiny app that gives a quick view of the url - view - template relations of all URLS registered with the dispatcher

## Installation 

`pip install django-associations --upgrade`

## Use

### Enable

```python
INSTALLED_APPS = (
    ...
    'django_extensions',
)
```

### Add to Urls

```python
urlpatterns = [

]
```

## What's new
 * It's now based on [django-extensions](https://github.com/django-extensions/django-extensions) since they implemented [show_urls](https://django-extensions.readthedocs.io/en/latest/command_extensions.html?highlight=show_urls#current-command-extensions) way better than deep inspect I used for my first version
 * React UI with quick search
 * Django Debug Toolbar panel (possibly)
 * Separate template loader/injection so that we can show window using hotkey (possibly overkill, but fun)

## Versioning

Follows Major Minor Hotfix system - starting at V2.0.0 since the first app is super depricated

## Django support

 * v3.0

