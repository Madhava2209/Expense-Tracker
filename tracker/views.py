from django.shortcuts import render,redirect
from tracker.models import *
from django.contrib.auth import *
# Create your views here.
def dashboard(request):
    user=request.user
    wallet=Wallet.objects.filter(user=user)
    expense=Expense.objects.filter(user=user)
    income=Income.objects.filter(user=user)

    return render(request,"dashboard.html",{"wallet":wallet,"expense":expense,"income":income})


def get_all_wallet(request):
    user=request.user
    all_wallet=Wallet.objects.filter(user=user)
    return render(request,"wallet.html",{"wallet":all_wallet})


def get_all_expense(request):
    user=request.user
    all_wallet=Wallet.objects.filter(user=user)
    all_expense=Expense.objects.filter(user=user)
    return render(request,"expense.html",{"expense":all_expense,"wallet":all_wallet})

def get_all_income(request):
    user=request.user
    all_wallet=Wallet.objects.filter(user=user)
    all_income=Income.objects.filter(user=user)
    return render(request,"income.html",{"income":all_income,"wallet":all_wallet})

def create_wallet(request):
    if request.method=="POST":
        wallet_name=request.POST["wallet_name"]
        wallet_balance=request.POST["wallet_balance"]

        wallet_instance=Wallet.objects.create(name=wallet_name,balance=wallet_balance,user=request.user)
        return redirect('/wallet/')

    return redirect("/wallet/")

def create_income(request):
    if request.method=="POST":
        title=request.POST["title"]
        income_instance=Wallet.objects.create(name=wallet_name,balance=wallet_balance,user=request.user)
        return redirect('/wallet/')

    return redirect("/wallet/")


def create_expense(request):

    return redirect('/expense/')