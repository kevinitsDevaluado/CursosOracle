
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
from core.erp.models import SubirTarea
#llamada a los forms
from core.erp.forms import SubirTareaForm
#mixin
from core.erp.mixins import IsSuperuserMixin,ValidatePermissionRequiredMixin

class SubirTareaListView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = SubirTarea
    template_name = "SubirTarea/list.html"
    permission_required = 'view_subirtarea'
        
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
                for i in SubirTarea.objects.all():
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
        context['tittle'] = 'SubirTarea'
        context['create_url'] = reverse_lazy('erp:subirtarea_create')
        context['list_url'] = reverse_lazy('erp:subirtarea_list')
        context['entity'] = 'SubirTarea'
        return context

class SubirTareaCreateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,CreateView):

    model = SubirTarea
    form_class = SubirTareaForm
    template_name = 'SubirTarea/create.html'
    success_url = reverse_lazy('erp:silabo_list')
    permission_required = 'add_subirtarea'
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
        context['tittle'] = 'Creacion de Subir Tarea'
        context['entity'] = 'SubirTarea'
        context['list_url'] = reverse_lazy('erp:silabo_list')
        context['action'] = 'add'
        return context

class SubirTareaUpdateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,UpdateView):
    model = SubirTarea
    form_class = SubirTareaForm
    template_name = 'SubirTarea/create.html'
    success_url = reverse_lazy('erp:subirtarea_list')
    permission_required = 'change_subirtarea'
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
        context['tittle'] = 'Edicion de Subir Tarea'
        context['entity'] = 'SubirTarea'
        context['list_url'] = reverse_lazy('erp:subirtarea_list')
        context['action'] = 'edit'
        return context

class SubirTareaDeleteView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,DeleteView):
    model = SubirTarea
    template_name = 'SubirTarea/delete.html'
    success_url = reverse_lazy('erp:subirtarea_list')
    permission_required = 'delete_subirtarea'
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
        context['tittle'] = 'Eliminacion de Subir Tarea'
        context['entity'] = 'SubirTarea'
        context['list_url'] = reverse_lazy('erp:subirtarea_list')
        return context
#VALIDARA LO FORMULARIOS
class SubirTareaformView(FormView):
    form_class = SubirTareaForm
    template_name = 'SubirTarea/create.html'
    success_url = reverse_lazy('erp:subirtarea_list')

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self,form):
        
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'FORM || SubirTarea'
        context['entity'] = 'SubirTarea'
        context['list_url'] = reverse_lazy('erp:subirtarea_list')
        return context

