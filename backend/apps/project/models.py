from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=40, help_text="项目名称")
    link = models.URLField(help_text="项目链接")
    slogan = models.CharField(max_length=256, help_text="标语")

    class Meta:
        verbose_name = "项目"
