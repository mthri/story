from django.apps import AppConfig


class StoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'story'
    verbose_name = 'داستان ها'

    def ready(self):
        from . import signals
