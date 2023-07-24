from django.db import models
kinds = [('l','lion'),('e','elephant')]
# Create your models here.
class Positions(models.Model):
    name = models.CharField(max_length=40)
    wage = models.IntegerField()

    def __str__(self):
        return self.name

class Employees(models.Model):
    age = models.IntegerField()
    position = models.ForeignKey(Positions,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return self.name+" "+self.surname

class Cages(models.Model):
    categoriesOfCages = [('s','small'),('m','medium'),('l','large')]
    category = models.CharField(choices=categoriesOfCages,max_length=10)
    caretaker = models.ForeignKey(Employees,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return str(self.category).upper() + " " + str(self.id)

class Animals(models.Model):
    name = models.CharField(max_length=20)
    kind = models.CharField(choices=kinds,max_length=20)
    additionalInfo = models.TextField(max_length=300)
    cage = models.ForeignKey(Cages,on_delete=models.SET_NULL,null=True)