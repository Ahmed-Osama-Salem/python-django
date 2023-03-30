from django.shortcuts import render
# Create your views here.

#Every function has a url
def index(req):
    user_db = {"name": "ahmed"}
    return render(req,"pages/index.html",user_db)