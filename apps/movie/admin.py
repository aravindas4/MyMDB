from django.apps import apps
from django.contrib import admin

from apps.utils.admin import DynamicColumnAdmin

my_app = apps.get_app_config('movie')

for model in list(my_app.get_models()):
    admin.site.register(model, DynamicColumnAdmin)