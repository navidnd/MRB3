from django import forms
from .models import mainPlanInfo, eachPlanDayInfo

class mainPlanForm  (forms.ModelForm):
    class Meta:
        model = mainPlanInfo
        fields = ['plan_name', 'start_date', 'end_date', 'duration']

