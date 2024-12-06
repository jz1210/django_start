from django.db import models

# Create your models here.
class Article(models.Model):
    # Article ID
    article_id = models.AutoField(primary_key=True)
    # Article title
    title = models.TextField()
    # Article brief content
    brief_content = models.TextField()
    # Article content
    content = models.TextField()
    # Article release date
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title