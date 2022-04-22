from django.conf import settings
from django.contrib.auth.decorators import login_required
from base64 import b64decode
from django.shortcuts import redirect, render
from .models import *
import uuid
from .skintone import *


def home(request):
    return render(request, 'pages/home.html')


def camera(request):
    if request.user.is_authenticated:
        return render(request, 'pages/camera.html')
    else:
        return redirect('login')


def upload_webcam_blob(blob, id):
    with open(f'media/uploads/{id}.png', 'wb') as fh:
        # Get only revelant data, deleting "data:image/png;base64,"
        data = blob.split(',', 1)[1]
        fh.write(b64decode(data))
        return fh


def screenshot(request):
    if request.method == "POST":
        id = str(uuid.uuid4())
        img = request.POST.get('image')
        upload_webcam_blob(img, id)
        link = f"uploads/{id}.png"
        image = Image_upload(img_id=id, image=link)
        image.save()
        request.session['id'] = id
        request.session['image'] = img
        return redirect('result')
    else:
        return redirect('camera')


def result(request):
    id = request.session['id']
    img = Image_upload.objects.filter(img_id=id).first()
    # url = f"{settings.BASE_DIR}/media/{img.image.url}"
    url = request.session['image']
    result = skintone(url)[0]
    return render(request, 'pages/result.html', {'image': img, 'result': result})
