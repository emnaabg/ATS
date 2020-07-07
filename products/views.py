from django.shortcuts import render
import urllib.request, json 
from products.models import *

# Create your views here.
def allproducts(request):
    
    with urllib.request.urlopen("http://test.ats-digital.com:3000/products?size=100") as url:
        data = json.loads(url.read().decode())
        
    for i in range(len(data["products"])):
        l=list()
        for key, value in data["products"][i].items() :
            if (key!="reviews"):
                l.append(value)
            else:
                for j in range (len(value)):
                    g=[i]
                    for ke, val in value[j].items() :
                        g.append(val)
                    r=review.objects.create(idproducton=g[0],rating=g[1],content=g[2])       
                    r.save()  

        d=production.objects.create(color=l[0],category=l[1],productName=l[2],price=l[3],description=l[4],tag=l[5],productMaterial=l[6],imageUrl=l[7],createdAt=l[8])       
        d.save()    

        pr=production.objects.all()
        context ={'products':pr}


    return render(request,'products/products.html',context)


def oneproduct(request,id):
        
    p=production.objects.get(id=id) 
        
    context ={'productinfo':p}

        
    return render(request,'products/productinfo.html',context)