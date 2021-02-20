
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
from core.erp.models import Alumno
#llamada a los forms
from core.erp.forms import AlumnoForm
#mixin
from core.erp.mixins import IsSuperuserMixin,ValidatePermissionRequiredMixin

class AlumnoListView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = Alumno
    template_name = "Alumno/list.html"
    permission_required = 'view_alumno'
    

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
                for i in Alumno.objects.all():
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
        context['tittle'] = 'Listado de Alumno'
        context['create_url'] = reverse_lazy('erp:alumno_create')
        context['list_url'] = reverse_lazy('erp:alumno_list')
        context['entity'] = 'Alumno'
        return context
        

class AlumnoCreateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,CreateView):

    model = Alumno
    form_class = AlumnoForm
    template_name = 'Alumno/create.html'
    success_url = reverse_lazy('erp:alumno_list')
    permission_required = 'add_alumno'
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
        context['tittle'] = 'Creacion de Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class AlumnoUpdateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'Alumno/create.html'
    success_url = reverse_lazy('erp:alumno_list')
    permission_required = 'change_alumno'
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
        context['tittle'] = 'Edicion de Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class AlumnoDeleteView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,DeleteView):
    model = Alumno
    template_name = 'Alumno/delete.html'
    success_url = reverse_lazy('erp:alumno_list')
    permission_required = 'delete_alumno'
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
        context['tittle'] = 'Eliminacion de Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = self.success_url
        return context
#VALIDARA LO FORMULARIOS
class AlumnoformView(FormView):
    form_class = AlumnoForm
    template_name = 'Alumno/create.html'
    success_url = reverse_lazy('erp:alumno_list')

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self,form):
        
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'FORM || Alumno'
        context['entity'] = 'Alumno'
        context['list_url'] = self.success_url
        return context