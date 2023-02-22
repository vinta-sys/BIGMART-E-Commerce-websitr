from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from backend.models import admindb,itemdb,prodb,admin
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def index(request):
    return render(request, "index.html")


def Addadmin(request):
    return render(request, "Addadmin.html")


def SaveAdmin(request):
    if request.method == 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        img = request.FILES['image']
        obj = admindb(Name=na, Email=em, Mobile=mo, Username=us, Password=pa, image=img)
        obj.save()
        return redirect(Addadmin)

def DisplayAdmin(request):
    data = admindb.objects.all()
    return render(request, "DisplayAdmin.html", {'data': data})

def editadmin(req, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req, "editadmin.html", {'data':data})

def updatedata(request,dataid):
    if request.method== 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(Name=na, Email=em, Mobile=mo, Username=us, Password=pa, image=file)
        return redirect(DisplayAdmin)

def deletedata(request, dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayAdmin)





def categorypage(request):
    return render(request, "categorypage.html")


def saveitem(request):
    if request.method == 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Description')
        img = request.FILES['image']
        obj = itemdb(Name=na, Description=em, image=img)
        obj.save()
        return redirect(categorypage)

def displayitem(request):
    data = itemdb.objects.all()
    return render(request, "displayitem.html", {'data': data})

def edititem(req, dataid):
    data = itemdb.objects.get(id=dataid)
    print(data)
    return render(req, "edititem.html", {'data':data})

def updateitem(request,dataid):
    if request.method== 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Description')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= itemdb.objects.get(id=dataid).image
        itemdb.objects.filter(id=dataid).update(Name=na, Description=em, image=file)
        return redirect(displayitem)

def deleteitem(request, dataid):
    data = itemdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayitem)


def productpage(request):
    data=itemdb.objects.all()
    return render(request, "productpage.html", {'data':data} )


def saveproduct(request):
    if request.method == 'POST':
        ca = request.POST.get('category')
        pn = request.POST.get('productname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        em = request.POST.get('description')
        img = request.FILES['image']
        obj = prodb(category=ca,productname=pn,price=pr,quantity=qu, description=em, image=img)
        obj.save()
        return redirect(productpage)
def displayproduct(request):
    data = prodb.objects.all()
    return render(request, "displayproduct.html", {'data': data})
def editproduct(req, dataid):
    data = prodb.objects.get(id=dataid)
    da = itemdb.objects.all()
    print(data)
    return render(req, "editproduct.html", {'data':data, 'da':da})

def updateproduct(request,dataid):
    if request.method== 'POST':
        ca = request.POST.get('category')
        pn = request.POST.get('productname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        em = request.POST.get('description')

        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= prodb.objects.get(id=dataid).image
        prodb.objects.filter(id=dataid).update(category=ca,productname=pn,price=pr,quantity=qu, description=em, image=file)
        return redirect(displayproduct)

def deleteproduct(request, dataid):
    data = prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def loginpage(rqst):
    return render(rqst, "login.html")

def adminlogin(rqst):
    if rqst.method == "POST":
        username_r = rqst.POST.get('username')
        password_r = rqst.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(rqst, user)
                rqst.session['username']=username_r
                rqst.session['password']=password_r
                messages.success(rqst,"login successfully")
                return redirect(index)

            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def adminlogout(rqst):
    del rqst.session['username']
    del rqst.session['password']
    return redirect(loginpage)


def admintable(request):
    data = admin.objects.all()
    return render(request, "admintable.html", {'data': data})


def deleteadmin(request, dataid):
    data = admin.objects.filter(id=dataid)
    data.delete()
    return redirect(admintable)

