from django.shortcuts import render,redirect
from myapp.models import Employee
from .forms import EmployeeForm

# Create your views here.




# def emp(request):
#     if request.methodd=='POST':
#         form=EmployeeForm(request,POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/show')
#             except:
#                 pass
#         else:
#             form=EmployeeForm()
#             return render(request,'index.html',{'form':form})

# def reg(request):
#     if request.method=='POST':
#         obj=Employee()
#         obj.fullname=request.POST.get('fname')
#         obj.save()
#     return render(request,'myapp/reg.html')



# def view_reg(request):
#     obj=Employee.objects.all()
#     abc={
#         'x':obj
#     }
#     return render(request,'myapp/view.html',abc)



def display(request):
    x=2
    y=9
    z=x+y
    return render(request,'sum.html',{'data1':x,'data2':y,'data3':z})
