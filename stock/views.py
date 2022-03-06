from multiprocessing import context
from urllib import request
from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import render ,HttpResponse
from don.stock_predictor import checker, stock_res, lister

# Create your views here.
def index(request):
    return render(request , "index.html")


def stock(request):
    if request.method == "POST":
        stk = request.POST.get("stk")
        test, res = checker(stk)
        if test == "1":
            name , error, restt = stock_res(stk)
            boom = 1
            det = zip( name,error, restt)
            context = {
                
                "len" : det,
                "last" : res,
                "boom" : boom,
                "stk": stk


            }
            return render(request,"results.html", context)
        else:
            
            context = {
                "boom" : 420
            }
            
            return render(request ,"results.html", context)
         

    return render(request, "stock.html")

def results(request):
    context = {
        "boom" : 555
    }
    return render(request,"results.html", context)


def lists(request):
    name, fulname, indus = lister()
    all = zip (name,fulname,indus)
    context ={
        "all" : all
    }
    return render(request,"list.html", context)

def rck(request):
    
    stk = request.GET.get("stk")
    name , error, restt = stock_res(stk)
    boom = 1
    test, res = checker(stk)
    det = zip( name,error, restt)
    context = {
                
        "len" : det,
         "last" : res,
        "boom" : boom,
        "stk" : stk


    }
    return render(request,"results.html", context)

    