
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView, CreateView, UpdateView

from src.accounts.decorators import investor_required
from src.portal.business.models import Business, Project, Investor, Shares, Project_Investor

@method_decorator(investor_required, name='dispatch')
class InvestorDashboard(TemplateView):
    template_name = 'investor/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(InvestorDashboard, self).get_context_data(**kwargs)
        project = Project.objects.all()
        share = Shares.objects.all()
        project_investor=Project_Investor.objects.filter(investor_id=self.request.user.id)
        context['applied_project'] = project_investor.count()
        context['project_count'] = project.count()
        context['project_list'] = Project.objects.all()
        return context



@method_decorator(investor_required, name='dispatch')
class ProjectListView(ListView):
    model = Project
    template_name = 'investor/project_list.html'


@method_decorator(investor_required, name='dispatch')
class SelectShareView(CreateView):
    model = Shares
    template_name = 'investor/select_share.html' 
    fields = ['share', 'share_equity', 'share_value']
    success_url = reverse_lazy('investor:dashboard')

    def form_valid(self, form):
        select_share = Shares.objects.get(user=self.request.user)
        form.instance.share = select_share
        messages.success(self.request,'Shares collected Successfully')
        return super(SelectShareView, self).form_valid(form)



@method_decorator(investor_required, name='dispatch')

class ShareDetailView(ListView):
    model = Shares
    template_name = 'investor/share_detail.html' 



