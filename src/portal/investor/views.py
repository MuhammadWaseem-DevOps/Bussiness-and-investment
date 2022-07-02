
from django.contrib import messages
from django.shortcuts import render,redirect


# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import View,ListView, TemplateView, CreateView, UpdateView, DetailView
from . form import BuyShareForm
from src.accounts.decorators import investor_required
from src.portal.business.models import Business, Project, Investor, Shares, Project_Investor

@method_decorator(investor_required, name='dispatch')
class InvestorDashboard(TemplateView):
    template_name = 'investor/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(InvestorDashboard, self).get_context_data(**kwargs)
        project = Project.objects.all()
        share = Shares.objects.all()
        project_investor=Project_Investor.objects.all()
        context['applied_project'] = project_investor.count()
        context['project_count'] = project.count()
        context['project_list'] = Project.objects.all()
        context['object_list'] = Project_Investor.objects.filter(investor__user=self.request.user).all()[:10]
        return context



@method_decorator(investor_required, name='dispatch')
class ProjectListView(ListView):
    model = Shares
    template_name = 'investor/project_list.html'
    
    def get_queryset(self):
        return Shares.objects.filter(value__gt=0)




@method_decorator(investor_required, name='dispatch')
class BuyShareView(View):
    def get(self,request,pk,*args,**kwargs):
        form = BuyShareForm
        return render(request,'investor/buy_share.html')

    def post(self,request,pk,*args,**kwargs):

        # GET: required values
        form = BuyShareForm(request.POST)
        user_value = self.request.POST.get('value')
        # GET: share model values
        share = Shares.objects.get(id=pk)
        share_equity=share.percentage_equity
        share_value=share.value
        # CAL1: user calculations
        user_percentage=(int(user_value)/share_value)*100
        user_equity=(float(user_percentage)*float(share_equity))/100
        # user = request.user
        # user.value=user_value
        # user.percentage_equity=user_equity
        # user.save()
        # CAL2: project calculations
        user = request.user
        investor = Investor.objects.get(user = self.request.user)
        # project_inv = Project_Investor(
        #     investor=investor, share=share, value=user_value
        # )
        if int(user_value) <= int(share.value):
            project_investor,create = Project_Investor.objects.get_or_create(share=share,investor=investor)
            project_investor.value = int(user_value) + int(project_investor.value)
            project_investor.percentage_equity = float(project_investor.percentage_equity) + float(user_equity)
            project_investor.save()
            # project_inv.save()
            share.value=int(share_value)-int(user_value)
            share.percentage_equity=float(share_equity)-float(user_equity)
            share.sell_equity = float(share.sell_equity) + float(user_equity)
            share.save()
            return redirect('investor:dashboard')
        else:
            messages.error(request,'Enter a value less than or equall to')
            return redirect('investor:buy_share', pk)





@method_decorator(investor_required, name='dispatch')
class ShareDetailView(ListView):
    model = Project_Investor
    template_name = 'investor/share_detail.html' 

    def get_context_data(self, **kwargs):
        context = super(ShareDetailView, self).get_context_data(**kwargs)
        context['object_list'] = Project_Investor.objects.filter(investor__user=self.request.user)
        return context

@method_decorator(investor_required, name='dispatch')
class ViewShareDetail(DetailView):
    model = Project_Investor
    template_name = 'investor/share_view_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ViewShareDetail, self).get_context_data(**kwargs)
        p_i = self.get_object()
        print(p_i.share)
        print(p_i.share.project)
        print(p_i.share.project.business)
        print(p_i.value)
        print(p_i.percentage_equity)
        return context




