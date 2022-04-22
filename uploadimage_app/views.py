from pages.skintone import skintone
from pages.views import result
from django.shortcuts import render
from .models import Image_data
from .form import ImageForm
from PIL import Image
# Create your views here.
import base64


def image_to_data_url(filename):
    ext = filename.split('.')[-1]
    prefix = f'data:image/{ext};base64,'
    with open(filename, 'rb') as f:
        img = f.read()
    return prefix + base64.b64encode(img).decode('utf-8')


def upload(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            link = f"./{obj.image.url}"
            url = image_to_data_url(link)
            result = skintone(url)[0]
            return render(request, "upload/upload.html", {"obj": obj, 'result': result})
    else:
        form = ImageForm()
        img = Image_data.objects.all()
    return render(request, "upload/upload.html", {"img": img, "form": form})
