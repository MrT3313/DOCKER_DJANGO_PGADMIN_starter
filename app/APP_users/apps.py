from django.apps import AppConfig

class AppUsersConfig(AppConfig):
    name = 'APP_users'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from APP_users import signals