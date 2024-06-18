from django.shortcuts import render
from django.http import HttpResponse
from .models import mainPlanInfo
from .forms import mainPlanForm


#main plans list

def createplan(request):
    form = mainPlanForm(request.POST or None)

    if form.is_valid():
        form.save()
    pass


#view all plans

def plans(request):
    mainsPlan_list = mainPlanInfo.objects.all()
    pass


def createplan(request):
    pass

#inside the main plan

def mainPlanInfo (request):
    form = mainPlanForm(request.POST or None)

    if form.is_valid():
        form.save()
        pass
    
    return HttpResponse("All done")


#edite plans

def update_plan(request,id):
    mainPlanInfo = mainPlanInfo.object.get(id=id)
    form = mainPlanForm(request.POST or None, instance=mainPlanInfo)

    if form.is_valid():
        form.save()
        pass

    pass

def delete_plan (request,id):
    mainPlanInfo = mainPlanInfo.object.get(id=id)

    if request.method == 'POST':
        mainPlanInfo.delete()
        pass

    pass






 