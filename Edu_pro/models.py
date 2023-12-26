from django.db import models

# Create your models here.
os_choice ={
    ('window_10','window_10'),
    ('window_8','window_8'),
    ('window_7','window_7'),
    ('ubuntu','ubuntu'),
    ('linux','linux'),
}
class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank = True,null = True)
    IP_address = models.CharField(max_length=30, blank = True,null = True)
    MAC_address = models.CharField(max_length=30, blank = True,null = True)
    users_name = models.CharField(max_length=30, blank = True,null = True)
    location = models.CharField(max_length=30, blank = True,null = True)
    os_model = models.CharField(choices = os_choice, blank = True,null = True,max_length=30,)
    export_to_CSV = models.BooleanField(default=False)
    purchase_date = models.DateField( auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)
def __unicode__(self):
    return self.computer_name
class ComputerHistory(models.Model):
     computer_name = models.CharField(max_length=30, blank=True, null=True)
     IP_address = models.CharField(max_length=30, blank=True, null=True)
     MAC_address = models.CharField(max_length=30, blank=True, null=True)
     os_model = models.CharField(choices = os_choice, blank = True,null = True,max_length=30,)
     users_name = models.CharField(max_length=30, blank=True, null=True)
     location = models.CharField(max_length=30, blank=True, null=True)
     purchase_date = models.DateField("Purchase Date(mm/dd/2019)", auto_now_add=False, auto_now=False, blank=True, null=True)
     timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)
class registration(models.Model):
   full_name= models.CharField(max_length=30)
   username=models.CharField(max_length=30)
   email= models.CharField(max_length=30)
   address = models.CharField(max_length=30)
   profile = models.ImageField(upload_to='images/',default='baba.jpg')
   co_password= models.CharField(max_length=30)
   password= models.CharField(max_length=30)




