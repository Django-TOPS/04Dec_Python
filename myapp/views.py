from django.shortcuts import render,redirect
from .models import signup, mynotes
from .forms import signupForm, mynotesForm
from django.contrib import auth
from django.contrib.auth import logout
from django.core.mail import send_mail
from twilio.rest import Client
import random
import requests
import json

# Create your views here.
def index(request):
    userdata=request.session.get("userdata")
    if request.method=='POST':
        mydata=signupForm(request.POST)
        if request.POST.get('signup')=='signup':
            if mydata.is_valid():
                mydata.save()
                request.session["userdata"]=request.POST['username']

                #Send Mail
                send_mail(f'Welcome, {request.POST["username"]}','Hello User, Your account has been created!','djangotestmail2021@gmail.com',['mohitbarai86@gmail.com','jenishdudhat135@gmail.com'])    

                print("Signup Successfully!")
                return redirect('notes')
            else:
                print(mydata.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']
            user=signup.objects.filter(username=unm,password=pas)

            userid=signup.objects.get(username=unm)
            if user:
                request.session["userdata"]=unm
                request.session['userid']=userid.id
                print("Login Successfully!")
                print("UserID:",userid.id)
                otp=random.randint(11111,99999)
                '''        
                #Send SMS using Twilio API
                
                client = Client('ACe7839bcf85f94e6471eeae0dca461239', '3712c876e5e8e28d89008a340365974f')
                message = client.messages.create(
                     body=f"Hello, {unm}. Welcome to mysite, Your One time password is {otp}",
                     from_='+14088728705',
                     to='+917984373369'
                 )

                print(message.sid)
                print("SMS Sent successfully!")
                '''

                url = "https://www.fast2sms.com/dev/bulkV2"
                
                # create a dictionary 
                my_data = { 
                    # Your default Sender ID 
                    'sender_id': 'FSTSMS',  
                    
                    # Put your message here! 
                    'message': f'Hello, {unm}. Your OTP is {otp}.',  
                    
                    'language': 'english', 
                    'route': 'q', 
                    
                    # You can send sms to multiple numbers 
                    # separated by comma. 
                    'numbers': '8980301250,8000367711,7622022511'    
                } 
                
                # create a dictionary 
                headers = { 
                    'authorization': 'eNB2jE9KVhwkSpvnfTIxudmyoHPXrJWQ3z76aFl8iAsCtR5OMb2EXaQmJ8tzi0brTIONRgHK5jZ9cMVs', 
                    'Content-Type': "application/x-www-form-urlencoded", 
                    'Cache-Control': "no-cache"
                }    
                response = requests.request("POST", 
                            url, 
                            data = my_data, 
                            headers = headers) 

                #load json data from source 
                returned_msg = json.loads(response.text) 
  
                # print the send message 
                print(returned_msg['message'])
                #print("SMS Sent successfully!")
                return redirect('notes')
            else:
                print('Login faild, Try again.')
    else:
        mydata=signupForm()
    return render(request,'index.html',{'userdata':userdata})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def notes(request):
    userdata=request.session.get("userdata")
    if request.method=='POST':        
        mydata=signupForm(request.POST)
        mynote=mynotesForm(request.POST, request.FILES)
        if request.POST.get('signup')=='signup':
            if mydata.is_valid():
                mydata.save()
                print("Signup Successfully!")
                print("SignupData:",mydata)
                request.session["userdata"]=request.POST['username']
                return redirect('notes')
            else:
                print(mydata.errors)
        elif request.POST.get('login')=='login':
            
            unm=request.POST['username']
            pas=request.POST['password']

            user=signup.objects.filter(username=unm,password=pas)
            userid=signup.objects.get(username=unm)
            if user:
                userdata=request.session.get("userdata")
                request.session["userdata"]=unm
                request.session['userid']=userid.id
                print("Login Successfully!")
                print("Via Notes USERID:",userid.id)
                return redirect('notes')
            else:
                print('Login faild, Try again.')
        elif request.POST.get('submit')=='submit':
                if mynote.is_valid():
                    mynote.save()
                    print("Your query has been uploaded!")
                    return redirect('/')
                else:
                    print(mynote.errors)
    else:
        mynote=mynotesForm()
    return render(request,'notes.html',{'userdata':userdata})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    loginid=request.session.get('userid')
    userdata=request.session.get('userdata')
    print("Current UserID is:",loginid)

    if request.method=='POST':
        updatefrm=signupForm(request.POST)
        myid=signup.objects.get(id=loginid)
        if updatefrm.is_valid():
            updatefrm=signupForm(request.POST,instance=myid)
            updatefrm.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(updatefrm.errors)
    else:
        updatefrm=signupForm()
    return render(request,'updateprofile.html',{'userdata':userdata,'loginid':signup.objects.get(id=loginid)})


def adminview(request):
    userdata=request.session.get("userdata")
    signupdata=signup.objects.all()
    return render(request,'admin.html',{'userdata':userdata,'signupdata':signupdata})

def deletedata(request, id):
    usrid=signup.objects.get(id=id)
    usrid.delete()
    return redirect('adminview')
   