from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .models import Post, PostImage, PremAlbum, Premium, Vip, VipAlbum, Category
from .forms import ContactForm

def main_view(request):
    return render(request, 'main.html')


def blog_view(request):
    posts = Post.objects.all()
    prems = Premium.objects.all()
    vips = Vip.objects.all()
    return render(request, 'blog.html', {'posts': posts, 'prems': prems, 'vips': vips})


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post': post,
        'photos': photos
    })


def create_post_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        post = Post.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            PostImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'create-post.html')


def premdetail_view(request, id):
    prem = get_object_or_404(Premium, id=id)
    photos = PremAlbum.objects.filter(post=prem)
    return render(request, 'detail.html', {
        'prem': prem,
        'photos': photos
    })


def create_prem_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        prem = Premium.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            PremAlbum.objects.create(
                post=prem,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createprem-post.html')


def vipdetail_view(request, id):
    vip = get_object_or_404(Vip, id=id)
    photos = VipAlbum.objects.filter(post=vip)
    return render(request, 'vipdetail.html', {
        'vip': vip,
        'photos': photos
    })


def create_vip_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        vip = Vip.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            VipAlbum.objects.create(
                post=vip,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createvip-post.html')


def catalog_view(request):
    categories = Category.objects.all()
    title = Category.name
    description = Category.description
    image = Category.image

    return render(request, 'catalog.html', {'categories': categories})


def contact_view(request):
    return render(request, 'contacts.html')


class AddContact(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")