from django.apps import apps

# Automatically import all models from all installed apps
for model in apps.get_models():
    globals()[model.__name__] = model

