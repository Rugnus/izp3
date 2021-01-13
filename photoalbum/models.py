from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title


class Premium(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class PremAlbum(models.Model):
    post = models.ForeignKey(Premium, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title


class Vip(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class VipAlbum(models.Model):
    post = models.ForeignKey(Vip, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title


class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    image = models.ImageField("Изображение", upload_to='../media/images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категерия'
        verbose_name_plural = 'Категории'
