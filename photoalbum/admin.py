from django.contrib import admin

from .models import Post, PostImage, Premium, PremAlbum, Vip, VipAlbum, Category


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


#-----------------

class PremAlbumAdmin(admin.StackedInline):
    model = PremAlbum


@admin.register(Premium)
class PremAdmin(admin.ModelAdmin):
    inlines = [PremAlbumAdmin]

    class Meta:
       model = Premium


@admin.register(PremAlbum)
class PremAlbumAdmin(admin.ModelAdmin):
    pass


#----------


class VipAlbumAdmin(admin.StackedInline):
    model = VipAlbum


@admin.register(Vip)
class VipAdmin(admin.ModelAdmin):
    inlines = [VipAlbumAdmin]

    class Meta:
       model = Vip


@admin.register(VipAlbum)
class VipAlbumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category)