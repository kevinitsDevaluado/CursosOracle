
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
from core.erp.models import NotasTarea
#llamada a los forms
from core.erp.forms import NotasTareaForm
#mixin
from core.erp.mixins import IsSuperuserMixin,ValidatePermissionRequiredMixin

class NotasTareaListView(LoginRequiredMixin ,ValidatePermissionRequiredMixin, ListView):
    
    model = NotasTarea
    template_name = "NotasTarea/list.html"
    permission_required = 'view_notastarea'
        
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
                for i in NotasTarea.objects.all():
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
        context['tittle'] = 'NotasTarea'
        context['create_url'] = reverse_lazy('erp:notastarea_create')
        context['list_url'] = reverse_lazy('erp:notastarea_list')
        context['entity'] = 'NotasTarea'
        return context

class NotasTareaCreateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,CreateView):

    model = NotasTarea
    form_class = NotasTareaForm
    template_name = 'NotasTarea/create.html'
    success_url = reverse_lazy('erp:notastarea')
    permission_required = 'add_notastarea'
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
        context['tittle'] = 'Creacion de NotasTarea'
        context['entity'] = 'NotasTarea'
        context['list_url'] = reverse_lazy('erp:notastarea_list')
        context['action'] = 'add'
        return context

class NotasTareaUpdateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,UpdateView):
    model = NotasTarea
    form_class = NotasTareaForm
    template_name = 'NotasTarea/create.html'
    success_url = reverse_lazy('erp:notastarea_list')
    permission_required = 'change_notastarea'
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
        context['tittle'] = 'Edicion de NotasTarea'
        context['entity'] = 'NotasTarea'
        context['list_url'] = reverse_lazy('erp:notastarea_list')
        context['action'] = 'edit'
        return context

class NotasTareaDeleteView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,DeleteView):
    model = NotasTarea
    template_name = 'NotasTarea/delete.html'
    success_url = reverse_lazy('erp:notastarea_list')
    permission_required = 'delete_notastarea'
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
        context['tittle'] = 'Eliminacion de Notas de Tarea'
        context['entity'] = 'NotasTarea'
        context['list_url'] = reverse_lazy('erp:notastarea_list')
        return context
#VALIDARA LO FORMULARIOS
class NotasTareaformView(FormView):
    form_class = NotasTareaForm
    template_name = 'NotasTarea/create.html'
    success_url = reverse_lazy('erp:notastarea_list')

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

