from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    # 用户学习的主题
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Python和Django在要将模型实例展示为纯文本对象时调用。
    def __str__(self):
        # 返回模型的字符串表示
        return self.text


class Entry(models.Model):
    # 学到有关某个主题的具体知识
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # ManyToManyField OneToOneField
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 模型的元数据即“所有不是字段的东西”，比如排序选项（ordering），数据库表名（db_table），或是阅读友好的单复数名（verbose_name和verbose_name_plural）。
        verbose_name_plural = 'entries'

    def __str__(self):
        # 返回模型的字符串表示
        return self.text[:50] + "..."

