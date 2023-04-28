from django.db import models


class KYC(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=(("M", "Male"), ("F", "Female")))
    date_of_birth = models.DateField()
    country = models.CharField(max_length=50)
    state_or_district = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_number_one = models.CharField(max_length=20)
    phone_number_two = models.CharField(max_length=20, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
