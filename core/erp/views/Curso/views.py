
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
#liberias models
from core.erp.models import Silabo
#llamada a los forms
from core.erp.forms import SilaboForm
from core.erp.models import Curso
#llamada a los forms
from core.erp.forms import CursoForm
#mixin
from core.erp.mixins import IsSuperuserMixin,ValidatePermissionRequiredMixin

class CursoListView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = Curso
    template_name = "Curso/list.html"
    permission_required = 'view_curso'
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
                for i in Curso.objects.all():
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
        context['tittle'] = 'Listado de Curso'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Curso'
        context['curso'] = self.get_queryset()   #agregamos la consulta al contexto
        #context['silabo'] = self.get_queryset()#context['form'] = self.form_class
        return context
    
           

class CursoCreateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,CreateView):

    model = Curso
    form_class = CursoForm
    template_name = 'Curso/create.html'
    success_url = reverse_lazy('erp:curso_list')
    permission_required = 'add_curso'
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
        context['tittle'] = 'Creacion de Una Curso'
        context['entity'] = 'Curso'
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['action'] = 'add'
        return context

class CursoUpdateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'Curso/create.html'
    success_url = reverse_lazy('erp:curso_list')
    permission_required = 'change_curso'
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
        context['tittle'] = 'Edicion de Un Curso'
        context['entity'] = 'Curso'
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['action'] = 'edit'
        return context

class CursoDeleteView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,DeleteView):
    model = Curso
    template_name = 'Curso/delete.html'
    permission_required = 'delete_curso'
    success_url = reverse_lazy('erp:curso_list')

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
        context['tittle'] = 'Eliminacion de Un Curso'
        context['entity'] = 'Curso'
        context['list_url'] = reverse_lazy('erp:curso_list')
        return context
#VALIDARA LO FORMULARIOS
class CursoformView(FormView):
    form_class = CursoForm
    template_name = 'Curso/create.html'
    success_url = reverse_lazy('erp:Curso_list')

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self,form):
        
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'FORM || Curso'
        context['entity'] = 'Curso'
        context['list_url'] = reverse_lazy('erp:curso_list')
        return context




class PerfilView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = Curso
    template_name = "Curso/perfil.html"
    permission_required = 'view_curso'

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
                for i in Curso.objects.all():
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
        context['tittle'] = 'Listado de Curso'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Curso'
        context['curso'] = self.get_queryset()   #agregamos la consulta al contexto
           #agregamos la consulta al contexto
        #context['form'] = self.form_class
        return context
    
           





class CursoListAView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = Curso
    template_name = "Curso/paralelos/list.html"
    permission_required = 'view_curso'

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
                for i in Curso.objects.all():
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
        context['tittle'] = 'Listado de Curso'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Curso'
        context['curso'] = self.get_queryset()   #agregamos la consulta al contexto
        #context['form'] = self.form_class
        return context
    
           

class CursoList2View(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = Curso
    template_name = "Curso/paralelos/list3.html"
    permission_required = 'view_curso'

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
                for i in Curso.objects.all():
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
        context['tittle'] = 'Listado de Curso'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Curso'
        context['curso'] = self.get_queryset()   #agregamos la consulta al contexto
        #context['form'] = self.form_class
        return context
    
           

class SilaboListView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = Silabo
    template_name = "Curso/perfil.html"
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
        context['tittle'] = 'Listado de Silabo'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Silabo'
        context['sila'] = self.get_queryset()   #agregamos la consulta al contexto
        #context['form'] = self.form_class
        return context

