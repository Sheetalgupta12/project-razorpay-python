from django.shortcuts import render
from .models import apple
import razorpay

from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100
        client=razorpay.Client(auth=("rzp_test_ZmPmQOgVrRvcfL","PeoJBLkhLIFzaC4YmDJ3yO4Y"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        apple1=apple(name=name,amount=amount,payment_id=payment['id'])
        apple1.save()
        return render(request,"index.html",{'payment':payment})
    return render(request,"index.html")

# Create your views here.
@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        order_id=""
        for key,val in a.items():
           if key=="razorpay_order_id":
               order_id=val
               break
           user=apple.objects.filter(payment_id=order_id).first()
           print(user)
           #user.paid=1
    return render(request,"success.html")


