from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .import models
from .import forms
from django.contrib import messages
import csv
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	title = 'Welcome: To the Stoke managment'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)
# @login_required
def Stocklist(request):
        title = "List of Items"
        form = forms.StockSearchForm(request.POST or None)
        queryset = models.Stock.objects.all()
        context = {
            "queryset": queryset,
            "title":title
        }
        if request.method == 'POST':
         queryset = models.Stock.objects.filter(category__icontains=form['category'].value(),
                                        item_name__icontains=form['item_name'].value()
                                        )
		 
         if form['export_to_CSV'].value() == True:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
                writer = csv.writer(response)
                writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
                instance = queryset
                for stock in instance:
                    writer.writerow([stock.category, stock.item_name, stock.quantity])
                return response

        context = {
        "form": form,
        "queryset": queryset,
		"title":title
    }
        return render(request, "Storelist.html",context)
        
#  form = forms.StockSearchForm(request.POST or None)
    #  context = {
    #            "form": form,
    #            "title": title,
    #            "queryset": queryset,

    #  }

    #  if request.method == 'POST':
    #       queryset = models.Stock.objects.all().filter(category__icontains=form['category'].value(),item_name__icontains=form['item_name'].value())
    #       if(queryset.exists):
    #            context = {
    #                 "form": form,
    #                 "title": title,
    #                 "queryset": queryset,
    #            }
    #            if form['export_to_CSV'].value() == True:
    #                 response = HttpResponse(content_type='text/csv')
    #                 response['Content-Disposition'] = 'attachment; filename="storelist.csv"'
    #                 writer = csv.writer(response)
    #                 writer.writerow(['Category', 'Item_name','Quantity'])
    #                 instance = queryset
    #                 for row in instance:
    #                   writer.writerow(['category', 'item_name','quantity'])
    #                 return response
    #       else:
    #            queryset = models.Computer.objects.all()
    #            context = {
    #            "form": form,
    #            "title": title,
    #            "queryset": queryset,
    #            }
    #            if form['export_to_CSV'].value() == True:
    #                 response = HttpResponse(content_type='text/csv')
    #                 response['Content-Disposition'] = 'attachment; filename="Records.csv"'
    #                 writer = csv.writer(response)
    #                 writer.writerow(['category', 'item_name','quantity'])
    #                 instance = queryset
    #                 for row in instance:
    #                      writer.writerow([row.category, row.item_name, row.quantity])
    #                 return response
    #  return render(request, "Storelist.html",context)
# @login_required
def add_items(request):
	form = forms.StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request,"Item Added Successfully")
		return redirect('/list_items')
	context = {
		"form": form,
		"title": "Add Item",
	}
	return render(request, "add_item.html", context)
# @login_required
def update_items(request,id):
	queryset = models.Stock.objects.get(id=id)
	form = forms.StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = forms.StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request,"Item updated Successfully")
			return redirect('/list_items')

	context = {
		'form':form
	}
	return render(request, 'add_item.html', context)
def delete_items(request,id):
	queryset = models.Stock.objects.get(id=id)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request,"Item Deleted Successfully")
		return redirect('/list_items')
	return render(request, 'delete_items.html')
def stock_detail(request, id):
	queryset = models.Stock.objects.get(id=id)
	context = {
		"title": queryset.item_name,
		"queryset": queryset,
	}
	return render(request, "item_deteil.html", context)
def issue_items(request, id):
	queryset = models.Stock.objects.get(id=id)
	form = forms.IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
		"username": 'Issue By: ' + str(request.user),
	}
	return render(request, "add_item.html", context)



def receive_items(request,id):
	queryset = models.Stock.objects.get(id=id)
	form = forms.ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "add_item.html", context)

def reorder_level(request,id):
	queryset = models.Stock.objects.get(id=id)
	form = forms.ReorderLevelForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))

		return redirect("/list_items")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_item.html", context)