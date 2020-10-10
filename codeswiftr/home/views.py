from django.shortcuts import render
from .models import AppLanding
# Create your views here.
from contact_us.forms import ContactForm



def demo(request):
    return render(request, 'home/landing.html')
    
def homepage(request):

    app = AppLanding.objects.all()[:1].get()

    if request.method == 'POST':
        form = ContactForm(request.POST, request=request)
        if form.is_valid():
            print("# form is valid")
            form.save()
            pass  # does nothing, just trigger the validation
        else:
            print("# form not valid")
    else:
        form = ContactForm(request=request)

    print(app.version, app.header.title)
    return render(request, 'home/base.html',
                  {
                      'app': app.header, 'main': app,
                      'download_info': app.download_info,
                      'features': app.features,
                      'about': app.about_info,
                      'reviews': app.reviews,
                      'screens': app.screens,
                      'form': form
                  })
