from django.shortcuts import render,redirect
from testapp.forms import EmployeeForm
from testapp.models import Employee

# Create your views here.


def fetch_data(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,"home.html",my_dict)

def insert_data(request):
    form=EmployeeForm()

    if request.method=="POST":
        form=EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("/home")


    my_dict={'form':form}
    return render(request,"insert.html",my_dict)

def delete_data(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/home')

def update_data(request,id):
    emp_data=Employee.objects.get(id=id)
    


    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=emp_data)
        if form.is_valid():
            form.save()
        return redirect("/home") 

    my_dict={'emp_data':emp_data}
    return render(request,"update.html",my_dict)


