from django.db import models

class Capabilities(models.Model):
    CAP_Id = models.AutoField(primary_key=True, unique=True)
    Name_of_capability = models.CharField(max_length=255)
    description_of_capability = models.TextField()

    def __str__(self):
        return f'{self.CAP_Id}- {self.Name_of_capability}'


class Templates(models.Model):
    TEMP_Id = models.AutoField(primary_key=True, unique=True)
    Name_of_template = models.CharField(max_length=255)
    capabilities = models.ManyToManyField(Capabilities)

    def __str__(self):
        return self.Name_of_template