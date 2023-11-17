from django.db import models
from random import randrange
from django.contrib import admin

# Create your models here.



CHARSET = '0123456789'
LENGTH = 5
MAX_TRIES = 100



Choice_Fields = (("Google Ads","Google Ads"),("Facebook Ads","Facebook Ads"),("Instagram Ads","Instagram Ads"),("Reels Ads","Reels Ads"),("Google My Business","Google My Business"))

class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'Category Name:{}'.format(self.name)
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return 'Product Name:  {}, Category Name:{}'.format(self.name,self.Category)


class Medium(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField( max_length = 20,
        choices = Choice_Fields)
    campaign_id = models.CharField(max_length=LENGTH, editable=False, unique=True)

    def __str__(self):
        return 'Product Name: {},{}, Medium:{},{}'.format(self.product_name.name,self.product_name.Category,self.name,self.campaign_id)

    
    def save(self,*args, **kwargs):
        if self.name == "Google Ads":
            print("Google Ads")
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ''
                    for i in range(LENGTH): 
                        new_code += CHARSET[randrange(  0, len(CHARSET))]
                    if not Medium.objects.filter(campaign_id=new_code):
                        self.campaign_id = str("GCA "+ new_code)
                        unique = True
                    loop_num += 1
                else:
                    raise ValueError("Couldn't generate a unique code.")
        if self.name == "Facebook Ads":
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ''
                    for i in range(LENGTH): 
                        new_code += CHARSET[randrange(  0, len(CHARSET))]
                    if not Medium.objects.filter(campaign_id=new_code):
                        self.campaign_id = str("FBA "+new_code)
                        unique = True
                    loop_num += 1
                else:
                    raise ValueError("Couldn't generate a unique code.")
            super(Medium, self).save(*args, **kwargs)
        if self.name == "Instagram Ads":
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ''
                    for i in range(LENGTH): 
                        new_code += CHARSET[randrange(  0, len(CHARSET))]
                    if not Medium.objects.filter(campaign_id=new_code):
                        self.campaign_id = str("INS "+new_code)
                        unique = True
                    loop_num += 1
                else:
                    raise ValueError("Couldn't generate a unique code.")
            super(Medium, self).save(*args, **kwargs)
        if self.name == "Reels Ads":
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ''
                    for i in range(LENGTH): 
                        new_code += CHARSET[randrange(  0, len(CHARSET))]
                    if not Medium.objects.filter(campaign_id=new_code):
                        self.campaign_id = str("REA "+new_code)
                        unique = True
                    loop_num += 1
                else:
                    raise ValueError("Couldn't generate a unique code.")
            super(Medium, self).save(*args, **kwargs)
        if self.name == "Google My Business":
            loop_num = 0
            unique = False
            while not unique:
                if loop_num < MAX_TRIES:
                    new_code = ''
                    for i in range(LENGTH): 
                        new_code += CHARSET[randrange(  0, len(CHARSET))]
                    if not Medium.objects.filter(campaign_id=new_code):
                        self.campaign_id = str("GMB "+new_code)
                        unique = True
                    loop_num += 1
                else:
                    raise ValueError("Couldn't generate a unique code.")
            super(Medium, self).save(*args, **kwargs)

class Medium_display(admin.ModelAdmin):
    list_display = ('product_name', 'name','campaign_id')