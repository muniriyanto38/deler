from django.shortcuts import render

def index(reguest):
    return render(reguest, 'kasir/index.html')