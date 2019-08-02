from django.shortcuts import render
from.models import ProductData
from django.http.response import HttpResponse
from.forms import ProductDataForm,UpdatingForm,DeletingForm


def home(request):
    return render(request,'home.html')


def insert(request):
    if request.method=="POST":
        pform=ProductDataForm(request.POST)
        if pform.is_valid():
            pnum=request.POST.get('product_number','')
            pname=request.POST.get('product_name','')
            pcost=request.POST.get('product_cost','')
            pclass=request.POST.get('product_class','')
            pweight=request.POST.get('product_weight','')
            data=ProductData(
                product_number=pnum,
                product_name=pname,
                product_cost=pcost,
                product_class=pclass,
                product_weight=pweight,
            )
            data.save()
            pform=ProductDataForm
            return render(request,'inserting.html',{'pform':pform})
    else:
        pform = ProductDataForm
        return render(request, 'inserting.html', {'pform': pform})


def updating(request):
    if request.method=="POST":
        uform=UpdatingForm(request.POST)
        if uform.is_valid():
            pnum=request.POST.get('product_number','')
            pcost=request.POST.get('product_cost','')
            pnum=ProductData.objects.filter(product_number=pnum)

            if not pnum:
                return HttpResponse("<h1>Data Is Not Available</h1>")
            else:
                pnum.update(product_cost = pcost)
                uform=UpdatingForm()
                return render(request,'updating.html',{'uform':uform})
        else:
            return HttpResponse("InvalidForm")
    else:
        uform = UpdatingForm()
        return render(request,'updating.html',{'uform': uform})


def retrieve(request):
    return render(request,'retrieve.html')


def deleting(request):
    if request.method=="POST":
        dform=DeletingForm(request.POST)
        if dform.is_valid():
            pnum=request.POST.get('product_number','')
            pnum=ProductData.objects.filter(product_number=pnum)

            if not pnum:
                return HttpResponse("<h1>Data Is Not Available</h1>")
            else:
                pnum.delete()
                dform=DeletingForm()
                return render(request,'deleting.html',{'dform':dform})
        else:
            return HttpResponse("InvalidForm")
    else:
        dform = DeletingForm()
        return render(request,'deleting.html',{'dform': dform})
