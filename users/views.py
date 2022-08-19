from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel


# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})
def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})




def UserHome(request):
    return render(request, 'users/UserHomePage.html', {})


def UserWeightLoss(request):
    if request.method=="POST":
        age = request.POST.get("age")
        vegnon = request.POST.get("vegnon")
        Weight = request.POST.get("Weight")
        Height = request.POST.get("Height")
        attr = [age,vegnon,Weight,Height]
        from .utility import dp_diet_process
        result = dp_diet_process.Weight_Loss(age,vegnon,Weight,Height)
        return render(request, "users/weightlossform.html",{"rslt": result})
    else:
        return render(request, "users/weightlossform.html",{})


def UserWeightGain(request):
    if request.method == "POST":
        age = request.POST.get("age")
        vegnon = request.POST.get("vegnon")
        Weight = request.POST.get("Weight")
        Height = request.POST.get("Height")
        attr = [age, vegnon, Weight, Height]
        from .utility import dp_diet_process
        result = dp_diet_process.Weight_Gain(age, vegnon, Weight, Height)
        return render(request, "users/weightgainform.html", {"rslt": result})
    else:
        return render(request, "users/weightgainform.html", {})



def UserHealthyResults(request):
    if request.method == "POST":
        age = request.POST.get("age")
        vegnon = request.POST.get("vegnon")
        Weight = request.POST.get("Weight")
        Height = request.POST.get("Height")
        attr = [age, vegnon, Weight, Height]
        from .utility import dp_diet_process
        result = dp_diet_process.Healthy(age, vegnon, Weight, Height)
        return render(request, "users/healthyform.html", {"rslt": result})
    else:
        return render(request, "users/healthyform.html", {})

