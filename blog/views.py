from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(requester):
    name="liu"
    t=datetime.now()
    return render(requester, "index.html", locals())
    pass
    pass

def register(requester):
    if requester.method == "POST":
        if requester.POST.get('user') == 'liu':
            return redirect("http://www.baidu.com")
        return HttpResponse("success!")
    return render(requester, "register.html")


def login(requester):
    return render(requester, "login.html")

def article_year(requester, year, mon):
    return HttpResponse(year)