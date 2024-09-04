from django.shortcuts import render
import requests


def index(request):
    response = requests.get("https://fakestoreapi.com/products")
    temp = []
    res = dict()
    for key, val in user.items():
        if val not in temp:
            temp.append(val)
            res[key] = val
            print("The dictionary after values removal : " + str(res))
    context= {
        "data":user
    }
    return render(request,"index.html",context)

def fashion(request):
    return render(request,"fashion.html")

def elctro(request):
    return render(request,"electronic.html")

def jewe(request):
    return render(request,"jewellery.html")