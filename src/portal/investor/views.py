from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from src.accounts.decorators import investor_required
from src.portal.business.models import Investor

@method_decorator(investor_required, name='dispatch')
class InvestorDashboard(ListView):
    model = Investor
    template_name = 'investor/dashboard.html'
