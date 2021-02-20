
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
#libreria JsonResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
#libreria decoradores
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#librerias views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, View
#liberias models
from core.erp.models import Matricula
#llamada a los forms
from core.erp.forms import MatriculaForm

from core.erp.mixins import IsSuperuserMixin,ValidatePermissionRequiredMixin
#PDF
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
class MatriculaListView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,ListView):
    model = Matricula
    template_name = "Matricula/list.html"
    permission_required = 'view_matricula'
    
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Matricula.objects.all():
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
        context['tittle'] = 'Matricula'
        context['create_url'] = reverse_lazy('erp:matricula_create')
        context['list_url'] = reverse_lazy('erp:matricula_list')
        context['entity'] = 'Matricula'
        context['matricula'] = self.get_queryset()
        return context
        
class MatriculaCreateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,CreateView):

    model = Matricula
    form_class = MatriculaForm
    template_name = 'Matricula/create.html'
    success_url = reverse_lazy('erp:matricula_list')
    permission_required = 'add_matricula'
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
        context['tittle'] = 'Agregar Matricula'
        context['entity'] = 'Matricula'
        context['list_url'] = reverse_lazy('erp:matricula_list')
        context['action'] = 'add'
        return context

class MatriculaUpdateView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'Matricula/create.html'
    success_url = reverse_lazy('erp:matricula_list')
    permission_required = 'change_matricula'
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
        context['tittle'] = 'Edicion de Instituto'
        context['entity'] = 'Institucion'
        context['list_url'] = reverse_lazy('erp:instituto_list')
        context['action'] = 'edit'
        return context

class MatriculaDeleteView(LoginRequiredMixin ,ValidatePermissionRequiredMixin,DeleteView):
    model = Matricula
    template_name = 'Matricula/delete.html'
    success_url = reverse_lazy('erp:matricula_list')
    permission_required = 'delete_profesor'
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
        context['tittle'] = 'Eliminacion de Matricula'
        context['entity'] = 'Matricula'
        context['list_url'] = reverse_lazy('erp:matricula_list')
        return context

#VALIDARA LO FORMULARIOS

class MatriculaformView(FormView):
    form_class = MatriculaForm
    template_name = 'Matricula/create.html'
    success_url = reverse_lazy('erp:matricula_list')

    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self,form):
        
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'FORM || Matricula'
        context['entity'] = 'Matricula'
        context['list_url'] = reverse_lazy('erp:matricula_list')
        return context

class SaleMatriculapdfView(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path
    
    def get(self, request, *args, **kwargs):
        try:
            
            template = get_template('Matricula/archivopdf.html')
            context = {
                'matricula': Matricula.objects.get(pk=self.kwargs['pk']),
                
                }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )

            return response
        except:
            pass
        return  HttpResponseRedirect(reverse_lazy('erp:matricula_list'))
