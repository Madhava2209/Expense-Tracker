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
        wallet_id=request.POST["wallet"]
        amount=request.POST["amount"]
        description=request.POST["description"]

        wallet_instance=Wallet.objects.get(pk=wallet_id)
        income_instance=Income.objects.create(
            user=request.user,
            title=title,
            wallet=wallet_instance,
            Amount=amount,
            description=description)
        wallet_instance.balance +=int(amount)
        wallet_instance.save()
        return redirect('/income/')

    return redirect("/income/")


def create_expense(request):
    if request.method=="POST":
        title=request.POST["title"]
        wallet_id=request.POST["wallet"]
        amount=request.POST["amount"]
        description=request.POST["description"]

        wallet_instance=Wallet.objects.get(pk=wallet_id)
        expense_instance=Expense.objects.create(
            user=request.user,
            title=title,
            wallet=wallet_instance,
            Amount=amount,
            description=description)
        wallet_instance.balance -=int(amount)
        wallet_instance.save()
        return redirect('/expense/')

    return redirect("/expense/")


def delete_wallet(request,wallet_id):
    wal=Wallet.objects.get(pk=wallet_id)
    wal.delete()
    return redirect("/wallet/")

def delete_income(request,income_id):
    inc=Income.objects.get(pk=income_id)
    inc.delete()
    return redirect("/income/")

def delete_expense(request,expense_id):
    exs=Expense.objects.get(pk=expense_id)
    exs.delete()
    return redirect("/expense/")

def edit_wallet(request,wallet_id):
    wal=Wallet.objects.get(pk=wallet_id)
    if request.method=="POST":
        
        name=request.POST["name"]
        balance=request.POST["balance"]
        

        wal.name=name
        wal.balance=balance
        wal.save()
        return redirect("/wallet/")

    return render(request,"edit_wallet.html",{"wal":wal})


def edit_income(request,income_id):
    inc=Income.objects.get(pk=income_id)
    wal=Wallet.objects.filter(user=request.user)
    if request.method=="POST":
        title=request.POST["title"]
        wallet_id=request.POST["wallet"]
        amount=request.POST["amount"]
        description=request.POST["description"]
        wallet_instance=Wallet.objects.get(pk=wallet_id)

        inc.title=title
        inc.wallet=wallet_instance
        inc.Amount=amount
        inc.description=description
        inc.save()
        return redirect("/income/"),

    return render(request,"edit_income.html",{"inc":inc,"wal":wal})


def edit_expense(request,expense_id):
    exs=Expense.objects.get(pk=expense_id)
    wal=Wallet.objects.filter(user=request.user)
    if request.method=="POST":
        title=request.POST["title"]
        wallet_id=request.POST["wallet"]
        amount=request.POST["amount"]
        description=request.POST["description"]
        wallet_instance=Wallet.objects.get(pk=wallet_id)

        exs.title=title
        exs.wallet=wallet_instance
        exs.Amount=amount
        exs.description=description
        exs.save()
        return redirect("/expense/"),

    return render(request,"edit_expense.html",{"exs":exs,"wal":wal})
