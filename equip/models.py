from django.db import models

CONDITIONS = (
    ('良好', '良好'),
    ('損壞但堪用', '損壞但堪用'),
    ('損壞待修', '損壞待修'),
    ('報廢', '報廢'))

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='名稱')

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name='名稱')

    def __str__(self):
        return self.name

class Equipment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='類型')
    manufacturer = models.CharField(max_length=100, verbose_name='製造商')
    model = models.CharField(max_length=100, verbose_name='型號')
    condition = models.CharField(max_length=100, choices=CONDITIONS, verbose_name='機況')
    description = models.TextField(blank=True, verbose_name='備註')
    image = models.CharField(max_length=200, blank=True, verbose_name='圖片網址')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='目前位置')

    def __str__(self):
        return "%s %s" % (self.manufacturer, self.model)