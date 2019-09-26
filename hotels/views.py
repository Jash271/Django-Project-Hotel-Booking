from django.shortcuts import render
from . import models
from django.http import Http404
from django.http import HttpResponse
import pdb
from django.core.mail import send_mail
# Create your views here.
def room(request):
    
    ro=models.rooms.objects.all()
    return render(request,"room.html",{"ro":ro})

def search(request):
    ro=models.rooms.objects.all()
    val1=request.POST['num1']
    
    return render(request,"search.html",{"ro":ro,"val1":val1})


def book(request,obj_id):
    request.session['val700']=obj_id
    return render (request,"booking.html")
    
        
    
    
def confirm(request):

     val8=int(request.POST['adult'])
     val10=int(request.POST['child'])
     val11=int(request.POST['nights'])
     
     cost=(val11*((val8*1000)+(val10*500)))
     request.session['val12']=request.POST['name']
     request.session['val2']=request.POST['adult']
     request.session['val3']=request.POST['child']
     request.session['val13']=request.POST['no']
     request.session['val9']=request.POST['room_code']
     request.session['val6']=request.POST['nights']
     request.session['val30']=request.POST['checkin']
     request.session['var']=cost
     request.session['val150']=request.POST['email']
     
     
     return render(request,"confirm.html",{'cost':cost})

     




def payment(request):
    
    
    cost=request.session['val700']
    
    return render(request,"Payment.html",{'cost':cost})


   
   


    
def success(request):
    
   
    guest1=models.guest()
    guest1.Head_name=request.session['val12']
    guest1.No_of_adults=request.session['val2']
    guest1.no_of_children=request.session['val3']
    guest1.Identity_no=request.session['val13']
    guest1.Room_code=request.session['val700']
    guest1.No_of_nights=request.session['val6']


    guest1.save()
    
    ro=models.rooms.objects.all()
    for ro in ro :
            if (ro.Roomcode==request.session['val700']):
                    ro.Availible=False
                    ro.save()
                    break
    val180=request.session['val150']
    send_mail('Payment Received','Room Booked','workjash@hushmail.com',['{}'.format(val180)],fail_silently=True)
    return render (request,"success.html")



    
    
    



