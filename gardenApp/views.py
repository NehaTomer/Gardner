from django.shortcuts import render,HttpResponseRedirect
from .models import*
def homepage(request):
    data=service.objects.all().order_by("id")
    teams=team.objects.all().order_by("id")
    testimonials=testimonial.objects.all().order_by("id")

    if (request.method=="POST"):
       q=quote()
       q.name=request.POST.get("name")
       q.email=request.POST.get("email")
       q.phone=request.POST.get("phone")
       q.service=request.POST.get("service") 
       q.message=request.POST.get("message")
       q.save() 
    return render(request,"index.html",{'data':data,'teams':teams,'testimonials':testimonials})
def aboutpage(request):
    teams=team.objects.all().order_by("id")
    return render(request,"about.html",{'teams':teams})
def servicepage(request):
    data=service.objects.all().order_by("id")
    return render(request,"service.html",{'data':data})
def projectpage(request):
    return render(request,"project.html")
def contactpage(request):
    if (request.method=="POST"):
       c=contact()
       c.name=request.POST.get("name")
       c.email=request.POST.get("email")
       c.subject=request.POST.get("subject") 
       c.message=request.POST.get("message")
       c.save()
    return render(request,"contact.html")
def featurepage(request):
    return render(request,"feature.html")
def quotepage(request):
    if (request.method=="POST"):
       q=quote()
       q.name=request.POST.get("name")
       q.email=request.POST.get("email")
       q.phone=request.POST.get("phone")
       q.service=request.POST.get("service") 
       q.message=request.POST.get("message")
       q.save() 
    return render(request,"quote.html")
def teampage(request):
    teams=team.objects.all().order_by("id")
    return render(request,"team.html",{'teams':teams})
def testimonialpage(request):
     if(request.method=="POST"):
         t=testimonial()
         t.name=request.POST.get("name")
         t.profession=request.POST.get("profession")
         t.message=request.POST.get("message")
         t.pic=request.POST.get("pic")
         t.save()
         return HttpResponseRedirect("/")
         
     return render(request,"testimonial.html")

def readmorepage(request,num):
    data=service.objects.get(id=num)

    return render(request,"readmore.html",{'data':data})