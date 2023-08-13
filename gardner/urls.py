
from django.contrib import admin
from django.urls import path
from gardenApp import views as garden
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',garden.homepage),
    path('about/',garden.aboutpage),
    path('service/',garden.servicepage),
    path('project/',garden.projectpage),
    path('contact/',garden.contactpage),
    path('feature/',garden.featurepage),
    path('quote/',garden.quotepage),
    path('team/',garden.teampage),
    path('testimonial/',garden.testimonialpage),
    path('readmore/<int:num>/',garden.readmorepage),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

