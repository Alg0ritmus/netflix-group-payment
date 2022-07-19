# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .mycode import *
from .models import *
from .decorators import *
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import Http404 



def index(request):
    list_of_vydavky = Vydavky.objects.all()
    context = {
            'list_of_vydavky' : list_of_vydavky,
        }
    return render(request,"mymoney/main.html",context)

@only_w_permission
def dash_board_get_Vydavky(request, vydavky_id):
    try:
        list_of_vydavky = Vydavky.objects.all()
        selected_vydavok = Vydavky.objects.filter(id=vydavky_id)[0].polozka_set.all()
        sumup = round(money_balance(selected_vydavok),2)
        output = ', '.join([i.name for i in list_of_vydavky])
        context = {
            'list_of_vydavky' : list_of_vydavky,
            'vydavky_string' : output,
            'vydavky_id': vydavky_id,
            'selected_vydavok': selected_vydavok,
            'sumup': sumup,
            'vydavok_meno':Vydavky.objects.get(pk=vydavky_id)
        }
        return render(request,"mymoney/mobileview.html",context)
    except:
        raise Http404("Nome kind of problem")

@only_w_permission
def pridaj_vydavky(request):
    if request.method == 'POST' and len((request.POST['vydavky']).strip(" "))>0:
        #request.POST['vydavky']
        new_object = Vydavky(name=request.POST['vydavky'])
        new_object.save()
        
    return redirect("../vydavky/1")

@only_w_permission
def pridaj_polozky(request,pridaj_polozky_id):
    if request.method == 'POST':
        selected_object = Vydavky.objects.get(pk=pridaj_polozky_id)
        #check suma
       
        if isfloat(request.POST['suma']) and len((request.POST['pub_date']).strip(" "))>0:
            suma=float(request.POST['suma'])
            poznamka = request.POST['poznamka']
            pub_date = request.POST['pub_date']
        else:
            return HttpResponse('<h1>Bad format for suma!</h1>')
        try:
            selected_object.polozka_set.create(suma=suma,poznamka=poznamka,pub_date=pub_date).save()

        except:
            return HttpResponse('<h1>Insufficient permission!</h1>')
    return redirect("../../vydavky/"+str(pridaj_polozky_id))

@only_w_permission
def vymaz_polozky(request,vymaz_polozky_id):
    if request.method == 'DELETE':
        request.method = 'GET'
        try:
            
            item = Polozka.objects.get(pk=vymaz_polozky_id)
            item.delete()
        except:
           
            return HttpResponse('<h1>Insufficient permission!</h1>')

@only_w_permission
def uprav_polozky(request,edit_polozky_id):
    selected_object = Polozka.objects.get(pk=edit_polozky_id)
    if request.method == 'POST':
        selected_object.suma = request.POST['suma']
        selected_object.poznamka = request.POST['poznamka']
        selected_object.pub_date = request.POST['pub_date']
        selected_object.save()
        # vydavok_id
        vydavky_id = Polozka.objects.get(pk=edit_polozky_id).vydavok.id

        return redirect("../../vydavky/"+str(vydavky_id))
    context = {
        'selected_object':selected_object
    }
    return render(request,"mymoney/edit.html",context) 

        




    