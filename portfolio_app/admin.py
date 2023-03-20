from django.contrib import admin
from django.apps import apps
'''
    Register each model referenced in models.__init__.py. Includes all portfolio_app models. 
    Used to dynamicaly add each model to the django admin panel.
'''
app = apps.get_app_config('portfolio_app')

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
