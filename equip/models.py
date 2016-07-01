from django.db import models
from django.contrib.auth.models import User

CONDITIONS = (
    ('良好', '良好'),
    ('損壞但堪用', '損壞但堪用'),
    ('損壞待修', '損壞待修'),
    ('報廢', '報廢'))

BELONGS_TO = (
    ('PA 組', 'PA 組'),
    ('學生會', '學生會'),
    ('PA 社', 'PA 社'),
    ('不分國界', '不分國界'),
    ('其他', '其他'))

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
    number = models.IntegerField(verbose_name='編號', default=0)
    condition = models.CharField(max_length=100, choices=CONDITIONS, verbose_name='機況')
    belongs_to = models.CharField(max_length=100, choices=BELONGS_TO, verbose_name='歸屬')
    description = models.TextField(blank=True, verbose_name='備註')
    image = models.CharField(max_length=200, blank=True, verbose_name='圖片網址')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='目前位置')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.manufacturer, self.model)

class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name='名稱')
    client = models.CharField(max_length=100, verbose_name='活動方名稱')
    location = models.CharField(max_length=100, verbose_name='活動地點')
    start_date = models.DateField(verbose_name='起始日期')
    end_date = models.DateField(verbose_name='結束日期')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='主控', related_name='manager_events')
    assistant = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='主控助理', related_name='assistant_events')
    stages = models.ManyToManyField(User, blank=True, verbose_name='Stage', related_name='stage_events')
    equipments = models.ManyToManyField(Equipment, verbose_name='借用器材')
    note = models.TextField(blank=True, verbose_name='備註')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name