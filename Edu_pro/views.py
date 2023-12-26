from django.shortcuts import render,redirect,get_object_or_404
from .import forms
from .import models
from django.http import HttpResponse
import csv
from django.contrib.auth import authenticate, login


def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def comp_list(request):
     title = 'list of all computers'
     queryset = models.Computer.objects.all()
     # form = forms.ComputerSearchForm(request.POST or None)
     # context = {
     #           "form": form,
     #           "title": title,
     #           "queryset": queryset,

     # }

     # if request.method == 'POST':
     #      queryset = models.Computer.objects.all().filter(computer_name__icontains=form['computer_name'].value(),users_name__icontains=form['users_name'].value())
     #      if(queryset.exists):
     #           context = {
     #                "form": form,
     #                "title": title,
     #                "queryset": queryset,
     #           }
     #           if form['export_to_CSV'].value() == True:
     #                response = HttpResponse(content_type='text/csv')
     #                response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
     #                writer = csv.writer(response)
     #                writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'os_model','users_name','location'])
     #                instance = queryset
     #                for row in instance:
     #                     writer.writerow([row.computer_name, row.IP_address, row.MAC_address, row.os_model, row.users_name, row.location])
     #                return response
     #      else:
     #           queryset = models.Computer.objects.all()
     #           context = {
     #           "form": form,
     #           "title": title,
     #           "queryset": queryset,
     #           }
     #           if form['export_to_CSV'].value() == True:
     #                response = HttpResponse(content_type='text/csv')
     #                response['Content-Disposition'] = 'attachment; filename="Records.csv"'
     #                writer = csv.writer(response)
     #                writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'os_model'])
     #                instance = queryset
     #                for row in instance:
     #                     writer.writerow([row.computer_name, row.IP_address, row.MAC_address, row.os_model, row.users_name, row.location])
     #                return response
     return render(request, "compList.html")
def entry(request):
     title ="Post Form"
     form = forms.ComputerForm(request.POST or None)
     if form.is_valid():
          form.save()
          return redirect('/list')
     context = {
          "form": form,
          "title": title,
     }
     return render(request, "entry.html", context)



def comp_edit(request,id):
     instance = get_object_or_404(models.Computer, id=id)
     form = forms.ComputerForm(request.POST or None, instance=instance)
     if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
          return redirect('/list')
     context = {
          "title": 'Edit ' + str(instance.computer_name),
          "instance": instance,
          "form": form,
     }
     return render(request, "entry.html", context)
def computer_delete(request, id=None):
   instance = get_object_or_404(models.Computer, id=id)
   if request.method == 'POST':
     instance.delete()
     return redirect("/list")
   return render(request,'delete.html')
def registration(request):
     title ="Registration Form"
     form = forms.RegistrationForm(request.POST or None)
     if form.is_valid():
          form.save()
          return redirect('/login')
     context = {
          "form": form,
          "title": title,
     }
     return render(request, "registration.html", context)
def login(request):
        form = forms.LoginForm(request.POST or None)
        title ="login Form"
        context={
             "title":title,
             "form":form
        }
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                
                login(request, user)
                return HttpResponse('/list')
        else:
          form = forms.LoginForm()
        return render(request, 'login.html', context)
def logout(request):
     logout(request)
     return redirect('/login')
