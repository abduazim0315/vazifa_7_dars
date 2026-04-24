from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Pk: {self.id}, name: {self.name}"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"

    def __repr__(self):
        return f"Pk: {self.id}, name: {self.model_name}"
