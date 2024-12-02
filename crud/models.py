from django.db import models
from django.core.validators import EmailValidator
from datetime import date
from django.core.exceptions import ValidationError

class Item(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key auto-generated
    name = models.CharField(max_length=100)
    email = models.CharField(
        max_length=255,
        validators=[EmailValidator(message="Enter a valid email address.")],
        unique=True  # Ensuring uniqueness of email
    )
    dob = models.DateField()  # Date of Birth

    def clean(self):
        # Ensure DOB is not in the future
        if self.dob > date.today():
            raise ValidationError("Date of birth cannot be in the future.")

    def __str__(self):
        return self.name
