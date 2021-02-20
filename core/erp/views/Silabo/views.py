
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
#libreria JsonResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
#libreria decoradores
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#librerias views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
#liberias models
from core.erp.models import Silabo
#llamada a los forms
from core.erp.forms import SilaboForm
#mixin
from core.erp.mixins import IsSuperuserMixin,ValidatePermissionRequiredMixin

class SilaboListView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = Silabo
    template_name = "Silabo/list.html"
    permission_required = 'view_silabo'
        
    @method_decorator(csrf_exempt)
    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Silabo.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)        
        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Silabo'
        context['create_url'] = reverse_lazy('erp:silabo_create')
        context['list_url'] = reverse_lazy('erp:silabo_list')
        context['entity'] = 'Silabo'
        return context

class SilaboCreateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,CreateView):

    model = Silabo
    form_class = SilaboForm
    template_name = 'Silabo/create.html'
    success_url = reverse_lazy('erp:silabo_list')
    permission_required = 'add_silabo'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    #def post(self, request, *args, **kwargs):
      #  form = CategoryForm(request.POST)
       # if form.is_valid():
        #    form.save()
         #   return HttpResponseRedirect(self.success_url)
        #self.object = None
        #context = self.get_context_data(**kwargs)
        #context['form'] = form
        #return render(request,self.template_name,context)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Creacion de Silabo'
        context['entity'] = 'Silabo'
        context['list_url'] = reverse_lazy('erp:silabo_list')
        context['action'] = 'add'
        return context

class SilaboUpdateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,UpdateView):
    model = Silabo
    form_class = SilaboForm
    template_name = 'Silabo/create.html'
    success_url = reverse_lazy('erp:silabo_list')
    permission_required = 'change_silabo'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Edicion de Silabo'
        context['entity'] = 'Silabo'
        context['list_url'] = reverse_lazy('erp:silabo_list')
        context['action'] = 'edit'
        return context

class SilaboDeleteView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,DeleteView):
    model = Silabo
    template_name = 'Silabo/delete.html'
    success_url = reverse_lazy('erp:silabo_list')
    permission_required = 'delete_silabo'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Eliminacion de Silabo'
        context['entity'] = 'Silabo'
        context['list_url'] = reverse_lazy('erp:silabo_list')
        return context
#VALIDARA LO FORMULARIOS
class SilaboformView(FormView):
    form_class = SilaboForm
    template_name = 'Silabo/create.html'
    success_url = reverse_lazy('erp:silabo_list')

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self,form):
        
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'FORM || Silabo'
        context['entity'] = 'Silabo'
        context['list_url'] = reverse_lazy('erp:silabo_list')
        return context

