from django.db import models


class List(models.Model):

    Item_Code = models.IntegerField(max_length=5, null=False, blank=False)
    Product_Name = models.CharField(max_length=300, null=False, blank=False)
    Poorvika_Price = models.CharField(max_length=25, blank=True, null=True)
    Flipkart_Price = models.CharField(max_length=25, blank=True, null=True)
    Amazon_Price = models.CharField(max_length=25, blank=True, null=True)
    Croma_Price = models.CharField(max_length=25, blank=True, null=True)
    Vijay_Sale_Price = models.CharField(max_length=25, blank=True, null=True)
    Reliance_Price = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.Item_Code, self.Product_Name, self.Poorvika_Price,\
            self.Flipkart_Price, self.Amazon_Price, self.Croma_Price, \
            self.Vijay_Sale_Price, self.Reliance_Price

    class Meta:
        verbose_name_plural = "Scraping Name"
