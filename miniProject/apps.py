from django.apps import AppConfig


class MiniprojectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miniProject'


    def ready(self):
        import miniProject.signals 