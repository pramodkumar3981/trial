from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category,Product,Newsletter,Profileusers,Contact,Gender
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,Group
from django.contrib import messages


# Create your views here.

# HOME PAGE
def home(request):
    cat_items = Category.objects.all()
    product_items = Product.objects.all()
    return render(request, 'home2.html', {'cat_items': cat_items,'product_items':product_items})

def home2(request):
    cat_items = Category.objects.all()
    product_items = Product.objects.all()
    return render(request, 'home2.html', {'cat_items': cat_items,'product_items':product_items})


#NEWS LETTER

def newsletter(request):
    if request.method == "POST":
        mailid = request.POST.get("mailid")
        Newsletter.objects.create(
            mailid=mailid
        )
        msg="Successfully Subscribe for Newsletter"
        return render(request,'newsletter.html',{'msg':msg})
    else:
        return render(request,'newsletter.html')

def signup(request):
    if request.method == "POST":
        first = request.POST.get("first")
        last = request.POST.get("last")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gender=request.POST.get("gender")
        city=request.POST.get("city")
        profile_pic=request.FILES.get("profile_pic")
        fs=FileSystemStorage()
        filename=fs.save(profile_pic.name,profile_pic)
        password = request.POST.get("password")
        user_obj = User(
            first_name = first,
            last_name = last,
            username = username,
            email = email
        )

        if User.objects.all().filter(email=email).exists():
            return render(request,'signup.html',{'msg':"This email address is already Exists"})
        else:
            user_obj.save()
            user_obj.set_password(password)
            user_obj.save()
            group = Group.objects.get(name='Normal')
            user_obj.groups.add(group)
            Profileusers.objects.create(
                user = user_obj,
                phone = phone,
                gender=gender,
                city=city,
                profile_pic=filename
            )
            # user authorization for access activities

            group = Group.objects.get(name='Normal')
            user_obj.groups.add(group)

            #message = messages.success("Registered Successfully Login Your Account ")

            return render(request,'signup.html',{'msg':'Your account has been activated successfully, You can now login.'})
    else:
        return render(request,'signup.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            subject = subject,
            message = message
        )
        return render(request,'contact.html',{'msg':'Thank you for getting in touch!'})
    return render(request,'contact.html')
@ login_required
def dashboard(request):
    cat_items = Category.objects.all()
    product_items = Product.objects.all()
    return render(request, 'dashboard.html', {'cat_items': cat_items, 'product_items': product_items})

def myaccount(request):
    current_user=Profileusers.objects.get(user__id=request.user.id)
    return render(request,'profilecard.html',{'current_user':current_user})

def updateuser(request):
    current_user=Profileusers.objects.get(user__id=request.user.id)
    if request.method=="POST":
        first = request.POST.get("first")
        last = request.POST.get("last")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        username=request.POST.get("username")
        city = request.POST.get("city")
        profile_pic = request.FILES.get("profile_pic")
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name,profile_pic)
        new_password = request.POST.get("password")
        user_obj=User.objects.get(id=request.user.id)
        user_obj.first_name=first
        user_obj.last_name=last
        user_obj.email=email
        user_obj.username=username
        user_obj.save()
        user_obj.set_password(new_password)
        try:
            user_obj.save()
            current_user.phone=phone
            current_user.gender=gender
            current_user.city=city
            current_user.profile_pic=filename
            current_user.save()
        except Exception as e:
            e="Something Missing Please Check again"
            return render(request,'updateprofileuser.html',{'e':e})
        else:
            msg="Profile Updates Successfully"
            return render(request,'updateprofileuser.html',{'current_user':current_user,'msg':msg})
    else:
        return render(request,'updateprofileuser.html')



def search(request):
    #prd=Product.objects.all()
    if request.method == 'POST':
        search=request.POST.get('search')
        result=Product.objects.filter(product_name__icontains=search)
        #context={'result':results}
        return render(request,'search.html',{'result':result})
    else:
        return render(request,'search.html')



