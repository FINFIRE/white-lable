from django.apps import AppConfig


class MatchingAlgorithmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Matching_Algorithm'

    def ready(self):
        import Matching_Algorithm.signals  # Import signals when app is ready
