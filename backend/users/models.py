from django.db import models



class CustomUser(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
   

    def __str__(self):
        return f"name: {self.name}"

   
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False, related_name="addresses")
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street} - {self.city}"



