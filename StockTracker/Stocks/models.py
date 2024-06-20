from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models

class Sectors(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=255, unique=True)
    sector_id = models.IntegerField(primary_key=True, default=1)  # Default value added
    isincode = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.name

class Stocks(models.Model):
    name = models.CharField(max_length=50)
    sectors = models.ManyToManyField(Sectors)  # Many-to-many relationship with Sectors
    symbol = models.CharField(max_length=255, unique=True)
    isincode = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True, default=1)  # Manually defining a default value for id

    def __str__(self):
        return self.name

class stock_user(AbstractUser):  # Asad code Do not touch!!!!!!
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=False)
    watchlist_sector = models.TextField()
    portfolio = models.TextField(default='[]') 
    closePosition= models.TextField(default='[]')
    
    class Meta:
        # Define the app_label to avoid conflicts in migrations
        app_label = 'Stocks'  # Replace 'your_app_name' with the actual name of your Django app

    # Specify unique related names for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='stock_user_groups',  # New related name for groups
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='stock_user_permissions',  # New related name for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )



class ContactInformation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=120)

    def __str__(self):
        return self.name

# models.py
from django.contrib.auth.models import AbstractUser

# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserProfile(AbstractUser):
    # Other fields if needed

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='user_profiles_groups',  # Updated related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='user_profiles_permissions',  # Updated related_name
    )

    def save(self, *args, **kwargs):
        # You don't need to manually set_password when extending AbstractUser
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

# models.py
from django.db import models

class FinancialData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    ema20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ema50 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ema100 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ema200 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rsi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.symbol} - {self.date}"
class SectorData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    ema20 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ema50 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ema100 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ema200 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rsi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rs = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Add other fields as needed

    def __str__(self):
        return f"{self.symbol} - {self.date}"

# Indicator count 
# models.py
from django.db import models    

class EmaCounts(models.Model):
    stock_data = models.ForeignKey(FinancialData, on_delete=models.CASCADE)
    ema20_output = models.IntegerField()
    ema50_output = models.IntegerField()
    ema100_output = models.IntegerField()
    ema200_output = models.IntegerField()
    rsi_output=models.IntegerField(null=True)
    rs_output=models.IntegerField(null=True)
    
    # Add other fields as needed


    def __str__(self):
        return f"{self.stock_data.symbol} - {self.stock_data.date}"

from django.db import models
from .models import SectorData

class EmaCountsSector(models.Model):
    stock_data = models.ForeignKey(SectorData, on_delete=models.CASCADE)
    ema20_output = models.IntegerField()
    ema50_output = models.IntegerField()
    ema100_output = models.IntegerField()
    ema200_output = models.IntegerField()
    rsi_output = models.IntegerField(null=True)
    rs_output = models.IntegerField(null=True)
    
    # Add other fields as needed

    def __str__(self):
        return f"{self.stock_data.symbol} - {self.stock_data.date}"


class Alert(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=50)
    closing_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Add any additional fields or methods as needed

    def __str__(self):
        return f"{self.symbol} - {self.date}"

class Main(models.Model):
    create_alert = models.CharField(max_length=10)  # Adjust max_length as needed
    trend = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expirationDate = models.DateField()
    name = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.name

