from django.db import models

class Applications(models.Model):
    L_id = models.IntegerField()
    Application_date = models.DateField()
    H_id = models.IntegerField()

    def __str__(self):
        return 'L_id:{0}'.format(self.L_id)

class Lsme(models.Model):
    L_id = models.IntegerField()
    Company = models.CharField(max_length=20)
    Sector = models.CharField(max_length=20)
    Location = models.CharField(max_length=20)
    No_of_employees_being_laid_off = models.IntegerField()

    def __str__(self):
        return self.Company

class Hsme(models.Model):
    H_id = models.IntegerField()
    Company = models.CharField(max_length=20)
    Sector = models.CharField(max_length=20)
    Location = models.CharField(max_length=20)
    No_of_employees_required = models.IntegerField()
    Years = models.IntegerField()
    Ready = models.CharField(max_length=10)
    Start_date = models.DateField()
    End_date = models.DateField()

    def __str__(self):
        return self.Company
