from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Transmission=(
    ('Automatic','Automatic'),
    ('Manual','Manual'),
)

Fuel_Type=(
    ('Gasoline','Gasoline'),
    ('Diesel','Diesel'),
    ('Biodiesel','Biodiesel'),
    )

Body_Style=(
    ('Sedan','Sedan'),
    ('Truck','Truck'),
    ('SUV','SUV'),
    )

   #  Car Table
class Car(models.Model):
    maker=models.ForeignKey('Maker',on_delete=models.CASCADE)
    catigory=models.ForeignKey('Catigory', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='car/img')
    model=models.CharField(max_length=30)
    year=models.IntegerField()
    color=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    transmission=models.CharField( max_length=50,choices=Transmission)
    fuel_type=models.CharField( max_length=50,choices=Fuel_Type)
    body_style=models.CharField( max_length=50,choices=Body_Style)
    create_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.model


    # kinds of cars
class Catigory(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
    # company that made the car
class Maker(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name