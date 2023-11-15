from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib import messages

from django.contrib.auth.models import User, auth
import requests as re
from .models import userpro, dcenter, order

from django.contrib.auth.decorators import login_required
import uuid
from .email import send


def index(request):
    return render(request, "index.html")


@login_required(login_url="registeruser")
def book(request):
    return render(request, "book.html")


@login_required(login_url="registeruser")
def orderr(request):
    if request.method == 'POST':
        address = request.POST['address']
        quantity = request.POST['quantity']
        image = request.FILES.get('filename')
        majority = request.POST['major']
        weight = request.POST['c']
        messag = request.POST['message']
        username = request.user.username
        orr = order.objects.filter(username=username)
        q = len(orr)
        orderid = username+"xy"+str(q)
        orde = order.objects.create(username=username, address=address, quantity=quantity,
                                    imgg=image, majority=majority, weight=weight, message=messag, orderid=orderid)
        orde.save()
    return render(request, "success.html")


@login_required(login_url="registeruser")
def myorders(request):
    username = request.user.username
    ordee = order.objects.filter(username=username)

    return render(request, "myorders.html", {"myorders": ordee})


def greencenter(request):
    df = {}
    pin = 000000
    if request.method == 'POST':
        pin = request.POST['pincode']
        df = dcenter.objects.filter(pincode=pin)

    return render(request, "greencenter.html", {"detail": df, "pin": pin, "len": len(df)})


@login_required(login_url="registeruser")
def logout(request):
    auth.logout(request)
    return redirect("/")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passs = request.POST['password']
        user = auth.authenticate(username=username, password=passs)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid details")
            return redirect('login')

    return render(request, "login.html")


def shop(request):
    return render(request, "shopping.html")


def gh(request):
    diseases = ""
    sy = []
    li = []
    x = pd.read_pickle(
        "C:/Users/Ankit/sqlconnect/connect/datadis.pkl")
    symptoms = x.columns.values
    sy = x.columns.values
    for index, value in enumerate(symptoms):
        symptom = " ".join([i.capitalize() for i in value.split("_")])
        li.append(symptom)

    return render(request, "cfgh.html", {"symptoms": li})


# def register(request):
#     postofficelist = []
#     a = 0
#     ab = {}

#     if request.method == 'POST':
#         pin = request.POST['pin']
#         df = re.get(
#             "https://www.postpincode.in/api/getPostalArea.php?pincode={}".format(pin))
#         ab = df.json()
#         # postofficelist = []
#         print(ab)
#         for o in range(len(ab)):
#             postofficelist.append(ab[o]['PostOfficeAddress'])
#         html_list = ''
#         for value in postofficelist:
#             html_list += '<option value="{0}">{0}</option>\n'.format(value)
#         # print(html_list)

#         htmlpl = """


#         <select>
#         {OPTIONS}
#         </select>

#         """.format(
#             OPTIONS=html_list,
#         )
#         # print(htmlpl)
#     return render(request, "register.html", {"lidd": postofficelist, "detail": ab})
def registeruser(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        username = request.POST['username']
        address = request.POST['address']
        pin = request.POST['pin']
        email = request.POST['email']
        passs = request.POST['passs']
        image = request.FILES.get('filename')
        pass2 = request.POST['pass2']
        if passs == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, 'Account already created . Please login !!!!')
                return redirect('registeruser')
            elif User.objects.filter(username=username).exists():
                messages.info(
                    request, 'Username already taken . Please try another !!!!')
                return redirect('registeruser')
            else:

                user = User.objects.create_user(
                    username=username, email=email, password=passs)
                user.save()
                # us = auth.authenticate(username=username, password=passs)
                # auth.login(request, us)
                userr = User.objects.get(username=username)
                profile = userpro.objects.create(

                    email_token=username, username=username, address=address, password=passs, pincode=pin, image=image)
                op = profile.email_token
                send(email, op)
                profile.save()
                return HttpResponse("Email sent for verification")
        else:
            messages.info(request, 'Enter same password in both')
            return redirect('registeruser')

    return render(request, 'userregister.html')


def verify(request, token):
    try:
        on = userpro.objects.get(email_token=token)
        on.isverified = True
        on.save()
        return HttpResponse('Verified')
    except Exception as e:
        return HttpResponse('Invalid Token')


def register(request):
    # if request.method == 'POST':
    #     fullname = request.POST['full']
    #     username = request.POST['username']
    #     phone = request.POST['phone']
    #     email = request.POST['email']
    #     passs = request.POST['password']
    #     pass2 = request.POST['password2']
    #     if passs == pass2:
    #         if picker.objects.filter(emaill=email).exists():
    #             messages.info(
    #                 request, 'Account already created . Please login !!!!')
    #             return redirect('register')
    #         elif picker.objects.filter(username=username).exists():
    #             messages.info(
    #                 request, 'Username already taken . Please try another !!!!')
    #             return redirect('register')
    #         else:
    #             user = picker.objects.create_user(name=fullname,
    #                                               username=username, emaill=email, password=passs, phone=phone)
    #             user.save()

    #             userr = picker.objects.get(username=username)
    #             # profile = pro.objects.create(userid=username, user=userr)
    #             userr.save()
    #             return redirect('/')
    #     else:
    #         messages.info(request, 'Enter same password in both')
    #         return redirect('register')

    return render(request, 'register.html')
