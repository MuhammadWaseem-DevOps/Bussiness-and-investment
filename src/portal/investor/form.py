from django.forms import ModelForm
from src.portal.business.models import Project_Investor
class BuyShareForm(ModelForm):
    class Meta:
        model = Project_Investor
        fields = ['value']