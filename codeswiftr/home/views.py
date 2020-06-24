from django.shortcuts import render
from .models import AppLanding
# Create your views here.


def homepage(request):
    app = AppLanding.objects.all()[:1].get()
    print(app.version, app.header.title)
    return render(request, 'home/base.html',
                  {'app': app.header, 'main': app,
                   'download_info': app.download_info,
                   'features': app.features,
                   'about': app.about_info
                   })
