from django.db import models
from django.conf import settings
# Create your models here.


# class User(models.Model):
#     username = models.CharField(max_length=15, default="", null=False)
#     first_name = models.CharField(max_length=20, default="", null=False)
#     last_name = models.CharField(max_length=30, default="", null=False)
#     email = models.EmailField(max_length=60, default="", null=False)
#     password = models.CharField(max_length=12, default="", null=False)
#
#     def __str__(self):
#         return self.first_name+" " +self.last_name


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=0, on_delete=models.CASCADE)
    CATEGORY_CHOICES = [
        ("CLO", "Clothing"),
        ("FOOD", "Food"),
        ("FUEL", "Fuel"),
        ("RENT", "Rent"),
        ("UTI", "Utilities"),
        ("PHN", "Phone"),
        ("EDU", "Education"),
        ("MISC", "Miscellaneous"),
    ]
    date = models.DateField('Date of expense', auto_now_add=False, blank=True, null=True)   # saved in format yyyy-mm-dd
    item = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, null=True, blank=True)
    amount = models.FloatField(null=False, blank=False)
    notes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)    # return expense id to the table on the django admin





