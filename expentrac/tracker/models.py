from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length = 15, default="", null=False)
    first_name = models.CharField(max_length=20, default="", null=False)
    last_name = models.CharField(max_length=30, default="", null=False)
    email = models.EmailField(max_length=60, default="", null=False)
    password = models.CharField(max_length=12, default="", null=False)

    def __str__(self):
        return self.first_name+self.last_name


class Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    date = models.DateField('Date expense incurred', auto_now_add=True)   # set 'auto_now_add to True if you want current time
    item = models.CharField(max_length=100)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, null=True)
    amount = models.FloatField()
    notes = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.user.id)





