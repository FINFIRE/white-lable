from django.db import models

class UserRoleChoices(models.TextChoices):
    SUPER_ADMIN = "SA", "Super Administrator" # dev's
    ADMIN = "ADM", "Administrator" # organization controller
    
    STAFF = "ST", "Staff" # staff of the organization
    USER = "USR", "User" # end user / customer
    



