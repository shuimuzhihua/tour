from django.db import models
from Route.models import Route

# Create your models here.


class Rt_Rq(models.Model):
    rt_id = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="线路ID")
    rq = models.DateField(verbose_name="日期")
    days = models.PositiveIntegerField(verbose_name="持续天数")

    def __str__(self):
        return f"Route ID: {self.rt_id} - Date: {self.rq}"

    class Meta:
        db_table = 'rt_rq'
        verbose_name = '线路日期对应'
        verbose_name_plural = '线路日期对应'
