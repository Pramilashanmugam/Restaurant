from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    """
    Configuration class for the reservations application.

    Attributes:
        default_auto_field (str): Specifies the type of primary key to use for
        models that do not define a primary key field.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservations'
