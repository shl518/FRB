from PIL import Image
from django.http import HttpResponse

from django.shortcuts import render, redirect
from app01 import models
from django.utils.safestring import mark_safe
import os
from django.conf import settings

initname = "test1"  # test img


# Create your views here.
def depart_list(request):
    page = int(request.GET.get('page', 1))
    pagesize = 10
    start = (page - 1) * pagesize
    end = page * pagesize
    total_count = models.Department.objects.all().count()
    queryset = models.Department.objects.all()[start:end]

    total_page, div = divmod(total_count, pagesize)
    if div:
        total_page += 1
    page_str_list = []
    for i in range(1, total_page + 1):
        ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(ele)
    page_string = mark_safe("".join(page_str_list))
    return render(request, 'depart_list.html', {'queryset': queryset, 'page_string': page_string})


def dpadd(request):
    if request.method == "GET":
        return render(request, 'dpadd.html')
    title = request.POST.get("title")

    file_object = request.FILES.get("avatar")
    img_path = os.path.join(settings.MEDIA_ROOT, title + ".png")
    models.Department.objects.create(title=title, path=img_path)
    print(img_path)
    f = open(img_path, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return redirect("/depart/list/")


def dpdelete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def mup():
    global initname
    initname = 'img'  # change init name
    path = os.path.join(settings.MEDIA_ROOT, "img.png")
    img = Image.open(path)
    img = img.convert('L')
    try:
        img.save(os.path.join(settings.MEDIA_ROOT, 'img.png'))
    except IOError:
        print("cannot convert")


def test(request):
    global initname
    if request.method == "GET":
        initname = request.GET.get('name')
        return render(request, 'index.html')
        # return HttpResponse("success")
    elif request.method == "POST":
        file_object = request.FILES.get('image')
        img_path = os.path.join(settings.MEDIA_ROOT, "img.png")
        f = open(img_path, mode='wb')
        for chunk in file_object.chunks():
            f.write(chunk)
        f.close()
        mup()
        return HttpResponse("success")


def load(request):
    print("load")
    global initname
    name = initname + '.png'
    print(name)
    img_path = os.path.join(settings.MEDIA_ROOT, name)
    with open(img_path, 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/png")


def commit(request):  # 111111111111111111
    global initname
    nname = request.GET.get('name')
    initname = nname
    img_path = os.path.join(settings.MEDIA_ROOT, nname + '.png')
    print(img_path)
    img = Image.open(img_path)
    img = img.convert('L')
    try:
        img.save(os.path.join(settings.MEDIA_ROOT, nname + '.png'))
    except IOError:
        print("cannot convert")
    return redirect("/test/?name=" + nname)


def loadresult(request):
    img_path = os.path.join(settings.MEDIA_ROOT, 'img.png')
    with open(img_path, 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/png")


def getpath(request):
    name = request.GET.get('name')
    newname = '/media/' + name + '.png'
    return HttpResponse(newname)


def getinitname(request):  # 图片初始化
    global initname
    name = initname + '.png'
    print(name)
    img_path = os.path.join(settings.MEDIA_ROOT, name)
    with open(img_path, 'rb') as f:
        image_data = f.read()
    print("readend")
    return HttpResponse(image_data, content_type="image/png")
