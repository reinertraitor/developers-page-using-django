from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # context = {'name': 'raaj', 'course': 'django'}
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['Address']
        city = request.POST['city']
        #print(name, email, password, city)
        contact = Contact( name=name ,email=email, password=password, address=address, city=city)  
        contact.save()
        print("the data has been saved")
        
    return render(request,'contact.html')
