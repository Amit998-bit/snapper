
from django.shortcuts import render,redirect
from snapperapp.models import Category, Product, Inquriy,Address
from django.contrib import messages
from django.http import HttpResponse


def Master(request):

     address =  Address.objects.all()

     context={
         
         'address':address,
     }
     return render(request,'master.html',context)
    


def Index(request):

    category = Category.objects.all()
    product = Product.objects.all()

    context={

        'category':category,
        'product':product,
    }

    return render(request,'index.html', context)


def Categry(request,bholenath):

    bholenath = bholenath.replace('_',' ')

    try:
     
     cat = Category.objects.get(name=bholenath)
     product = Product.objects.filter(cat=cat)

     return render(request, 'categories.html', {'product':product, 'category':cat})

    except:
     
      messages.success(request, (" that catgories is not display here"))
    return redirect('index')

   
   

    #return render(request, 'categry.html')


def Comapny(request):

    return render(request, 'company-profile.html')

def Compr(request):

    return render(request,'compression-series.html')

def Contact(request):

    if request.method=="POST":
           
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            ps = request.POST['ps']
            msg = request.POST['message']
           
            ct=Inquriy(name=name, email=email, mobile=mobile, ps=ps,  message=msg)
            
            ct.save()

            return HttpResponse("Your message is sucessfully sended !")
     
     
         #return render(request , 'contact.htm')

    return render(request,'contact.html')


def Search_item(request):

     if request.method=='POST':
         kailash = request.POST['kailash']
         product = Product.objects.filter(name__contains=kailash)

         return render(request, 'search-items.html',{'kailash':kailash,'product':product})

     else:
        
      return render(request, 'search-items.html')

def Sitemaps(request):

    return render(request,'sitemap.html')

def Privacy(request):

    return render(request,'privacy-policy.html')

def Terms(request):

    return render(request,'terms-and-conditions.html')

def Disclm(request):

    return render(request,'disclaimer.html')


