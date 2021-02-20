from django.urls import path
from core.erp.views.dashboard.views import DashboardView
from core.erp.views.categoria.views import categoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, CategoryformView
from core.erp.views.Instituto.views import InstitutoListView, InstitutoCreateView, InstitutoUpdateView, InstitutoDeleteView, InstitutoformView
from core.erp.views.Matricula.views import MatriculaListView, MatriculaCreateView, MatriculaUpdateView, MatriculaDeleteView, MatriculaformView, SaleMatriculapdfView
from core.erp.views.Silabo.views import SilaboListView, SilaboCreateView, SilaboUpdateView, SilaboDeleteView, SilaboformView
from core.erp.views.Profesor.views import ProfesorListView, ProfesorCreateView, ProfesorUpdateView, ProfesorDeleteView, ProfesorformView
from core.erp.views.Materia.views import MateriaListView, MateriaCreateView, MateriaUpdateView, MateriaDeleteView, MateriaformView
from core.erp.views.Alumno.views import AlumnoListView, AlumnoCreateView, AlumnoUpdateView, AlumnoDeleteView, AlumnoformView
from core.erp.views.SubirTarea.views import SubirTareaListView, SubirTareaCreateView, SubirTareaUpdateView, SubirTareaDeleteView, SubirTareaformView
from core.erp.views.NotasTarea.views import NotasTareaListView, NotasTareaCreateView, NotasTareaUpdateView, NotasTareaDeleteView, NotasTareaformView
from core.erp.views.Curso.views import CursoListView,PerfilView,CursoList2View,CursoListAView, CursoCreateView, CursoUpdateView, CursoDeleteView, CursoformView


app_name = 'erp'

urlpatterns = [
    path('category/list/', categoryListView.as_view(),name='category_list'),
    path('category/add/', CategoryCreateView.as_view(),name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(),name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(),name='category_delete'),
    path('category/form/', CategoryformView.as_view(),name='category_form'),
    #home Administration
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #INSTITUTO
    path('instituto/list/', InstitutoListView.as_view(),name='instituto_list'),
    path('instituto/add/', InstitutoCreateView.as_view(),name='instituto_create'),
    path('instituto/update/<int:pk>/', InstitutoUpdateView.as_view(),name='instituto_update'),
    path('instituto/delete/<int:pk>/', InstitutoDeleteView.as_view(),name='instituto_delete'),
    path('instituto/form/', InstitutoformView.as_view(),name='instituto_form'),
    #MATRICULA
    path('matricula/list/', MatriculaListView.as_view(),name='matricula_list'),
    path('matricula/add/', MatriculaCreateView.as_view(),name='matricula_create'),
    path('matricula/update/<int:pk>/', MatriculaUpdateView.as_view(),name='matricula_update'),
    path('matricula/delete/<int:pk>/', MatriculaDeleteView.as_view(),name='matricula_delete'),
    path('matricula/form/', MatriculaformView.as_view(),name='matricula_form'),
    #pdf
    path('matricula/pdf/<int:pk>/', SaleMatriculapdfView.as_view(),name='matricula_pdf'),   
    #SILABO
    path('silabo/list/', SilaboListView.as_view(),name='silabo_list'),
    path('silabo/add/', SilaboCreateView.as_view(),name='silabo_create'),
    path('silabo/update/<int:pk>/', SilaboUpdateView.as_view(),name='silabo_update'),
    path('silabo/delete/<int:pk>/', SilaboDeleteView.as_view(),name='silabo_delete'),
    path('silabo/form/', SilaboformView.as_view(),name='silabo_form'),
    #path('silabo/descarga/', SilaboDownloadView.as_view(),name='silabo_descarga'),
    #PROFESOR
    path('profesor/list/', ProfesorListView.as_view(),name='profesor_list'),
    path('profesor/add/', ProfesorCreateView.as_view(),name='profesor_create'),
    path('profesor/update/<int:pk>/', ProfesorUpdateView.as_view(),name='profesor_update'),
    path('profesor/delete/<int:pk>/', ProfesorDeleteView.as_view(),name='profesor_delete'),
    path('profesor/form/', ProfesorformView.as_view(),name='profesor_form'),
    #MATERIA
    path('materia/list/', MateriaListView.as_view(),name='materia_list'),
    path('materia/add/', MateriaCreateView.as_view(),name='materia_create'),
    path('materia/update/<int:pk>/', MateriaUpdateView.as_view(),name='materia_update'),
    path('materia/delete/<int:pk>/', MateriaDeleteView.as_view(),name='materia_delete'),
    path('materia/form/', MateriaformView.as_view(),name='materia_form'),
    #Alumno
    path('alumno/list/', AlumnoListView.as_view(),name='alumno_list'),
    path('alumno/add/', AlumnoCreateView.as_view(),name='alumno_create'),
    path('alumno/update/<int:pk>/', AlumnoUpdateView.as_view(),name='alumno_update'),
    path('alumno/delete/<int:pk>/', AlumnoDeleteView.as_view(),name='alumno_delete'),
    path('alumno/form/', AlumnoformView.as_view(),name='alumno_form'),
    #SUBIR TAREA 
    path('subirtarea/list/', SubirTareaListView.as_view(),name='subirtarea_list'),
    path('subirtarea/add/', SubirTareaCreateView.as_view(),name='subirtarea_create'),
    path('subirtarea/update/<int:pk>/', SubirTareaUpdateView.as_view(),name='subirtarea_update'),
    path('subirtarea/delete/<int:pk>/', SubirTareaDeleteView.as_view(),name='subirtarea_delete'),
    path('subirtarea/form/', AlumnoformView.as_view(),name='subirtarea_form'),
    #SUBIR TAREA 
    path('notastarea/list/', NotasTareaListView.as_view(),name='notastarea_list'),
    path('notastarea/add/', NotasTareaCreateView.as_view(),name='notastarea_create'),
    path('notastarea/update/<int:pk>/', NotasTareaUpdateView.as_view(),name='notastarea_update'),
    path('notastarea/delete/<int:pk>/', NotasTareaDeleteView.as_view(),name='notastarea_delete'),
    path('notastarea/form/', NotasTareaformView.as_view(),name='notastarea_form'),

    #CURSO  
    path('curso/list/', CursoListView.as_view(),name='curso_list'),
    path('curso/add/', CursoCreateView.as_view(),name='curso_create'),
    path('curso/update/<int:pk>/', CursoUpdateView.as_view(),name='curso_update'),
    path('curso/delete/<int:pk>/', CursoDeleteView.as_view(),name='curso_delete'),
    path('curso/form/', CursoformView.as_view(),name='curso_form'),
    #paralelos - SEGUNDO - TERCERO
    path('curso/lis_a/', CursoListAView.as_view(),name='curso_list_a'),
    path('curso/lis_2/', CursoList2View.as_view(),name='curso_list_2'),
    path('curso/perfil/', PerfilView.as_view(),name='curso_perfil'),
]