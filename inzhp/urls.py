
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from photoalbum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name="main"),
    path('blog/', views.blog_view, name='blog'),
    path('create-post/', views.create_post_view, name='create-post'),
    path('<int:id>/', views.detail_view, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
