from builtins import map
from config.settings import MEDIA_URL, STATIC_URL
from crum import get_current_user
from core.erp.choices import gender_choices, periodo_choices, paralelo_choices
from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from core.models import BaseModel, MatriculaModel
from core.user.models import User

# Create your models here.

# TABLA CATEGORIA --- PRUEBA


class Category(BaseModel):
    nombre = models.CharField(
        max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=150, null=True,
                            blank=True, verbose_name='Descripcion')

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Category, self).save()

    def toJSON(self):
        item = model_to_dict(self)

        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

# Create your models here.
# TABLA INSTITUTO -ADMIN


class Instituto(models.Model):

    nombre = models.CharField(max_length=100, verbose_name='Instituto')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo', unique=True)
    imagen = models.ImageField(
        upload_to='instituto/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return ' {}'.format(self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        item['imagen'] = self.get_image()
        return item
    # PARA PONER UNA IMAGEN POR default si no subieron una

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Instituto'
        verbose_name_plural = 'Institutos'
        ordering = ['id']
# TABLA CURSO

class Materia(BaseModel):
    nombre = models.CharField(max_length=100, verbose_name='Materia')
    #rama = models.CharField(max_length=100, verbose_name='Ramas')
    #idprofesor = models.OneToOneField(Profesor, on_delete=models.CASCADE)
    #idtarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    #idcurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    # +´+
    # idevaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Materia, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        #item['idprofesor'] = self.idprofesor.toJSON()
        return item

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['id']



class Curso(BaseModel):

    nivel = models.CharField(max_length=100, verbose_name='Nivel')
    Paralelo = models.CharField(
        max_length=100, choices=paralelo_choices, default='PARALELO A', verbose_name='Paralelo')
    mate = models.ForeignKey(Materia, on_delete=models.CASCADE)
    

    def __str__(self):
        return 'Nivel : %s Paralelo: %s' % (self.nivel, self.Paralelo)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Curso, self).save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['mate'])
        item['mate'] = self.mate.toJSON()
        return item


    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']


# PROFESOR .--------- NELL
class Profesor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    especialid = models.CharField(max_length=100, verbose_name='Especialidad')
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo', unique=True)
    imagen = models.ImageField(
        upload_to='Profesor/%Y/%m/%d', null=True, blank=True)
    #institucion = models.ForeignKey(Instituto, on_delete=models.CASCADE)

    def __str__(self):
        return ' {} {}'.format(self.nombre, self.apellido)

    def toJSON(self):
        item = model_to_dict(self)
        item['imagen'] = self.get_image()
        #item = model_to_dict(self, exclude=['imagen'])
        #item['imagen'] = self.document.url

        return item
    # PARA PONER UNA IMAGEN POR default si no subieron una

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['id']

# ALUMNO .------------------- NELL

class Alumno(models.Model):
    cedula = models.CharField(max_length=10, verbose_name='Cedula')
    nombre = models.CharField(max_length=100, verbose_name='Alumno')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo', unique=True)
    imagen = models.ImageField(
        upload_to='Alumno/%Y/%m/%d', null=True, blank=True)
    #institucion = models.ForeignKey(Instituto, on_delete=models.CASCADE)

    def _str_(self):
        return 'Nombre: {}'.format(self.nombre)

    def toJSON(self):
        item = model_to_dict(self)
        #item = model_to_dict(self, exclude=['imagen'])
        item['imagen'] = self.get_image()

        #item['imagen'] = self.document.url

        return item
    # PARA PONER UNA IMAGEN POR default si no subieron una

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['id']


class Matricula(BaseModel):

    periodo = models.CharField(max_length=30, choices=periodo_choices,
                               default='SEPTIEMBRE-FEBRERO', verbose_name='Periodo')
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    cur = models.ForeignKey(
        Curso, on_delete=models.CASCADE, verbose_name='Curso')

    def _str_(self):
        return self.fecha

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Matricula, self).save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['user_creation','cur','fecha'])
        item['user_creation'] = self.user_creation.toJSON()
        #item['insti'] = self.insti.toJSON()
        item['cur'] = self.cur.toJSON()
        #item['curso'] = [i.toJSON() for i in self.curs_set.all()]
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        ordering = ['id']




# crear tarea-
class Silabo(BaseModel):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    Descripcion = models.CharField(max_length=200, verbose_name='Descripcion')
    #matri = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    nota = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Nota', null=True, blank=True)
    
    document = models.FileField(
        upload_to='tareas/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Silabo, self).save()

    def toJSON(self):

        item = model_to_dict(self, exclude=['document'])
        #item['mate'] = self.mate.toJSON()
        item['document'] = self.document.url
        return item

    # PARA PONER UNA IMAGEN POR default si no subieron una
    # def get_image(self):
    #    if self.imagen:
    #        return '{}{}'.format(MEDIA_URL, self.imagen)
    #    return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Silabo'
        verbose_name_plural = 'Silabos'
        ordering = ['id']

# TESTS



class Deber(models.Model):
    tema = models.CharField(max_length=100, verbose_name='Tema')
    mate = models.ForeignKey(Materia, on_delete=models.CASCADE)
    alu = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    document = models.FileField(
        upload_to='deberes/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return 'Tema: {}'.format(self.tema)

    def toJSON(self):

        item = model_to_dict(self, exclude=['document'])
        item['mate'] = self.mate.toJSON()
        item['alu'] = self.alu.toJSON()
        item['document'] = self.document.url
        return item

    # PARA PONER UNA IMAGEN POR default si no subieron una
    # def get_image(self):
    #    if self.imagen:
    #        return '{}{}'.format(MEDIA_URL, self.imagen)
    #    return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Deber'
        verbose_name_plural = 'Deberes'
        ordering = ['id']


# crear alumno_tarea
class SubirTarea(BaseModel):
    
    tarea = models.FileField(
        upload_to='tareas/%Y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        return 'Id: {}'.format(self.id)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(SubirTarea, self).save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['user_creation','tarea'])
        item['user_creation'] = self.user_creation.toJSON()
        item['tarea'] = self.tarea.url
        return item

    # PARA PONER UNA IMAGEN POR default si no subieron una
    # def get_image(self):
    #    if self.imagen:
    #        return '{}{}'.format(MEDIA_URL, self.imagen)
    #    return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'SubirTarea'
        verbose_name_plural = 'SubirTareas'
        ordering = ['id']


# crear NotasTarea
class NotasTarea(BaseModel):
    tareaPre = models.ForeignKey(SubirTarea, on_delete=models.CASCADE)
    nota = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Nota', null=True, blank=True)
    observacion = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Observacion')

    def _str_(self):
        return 'Documento: {}'.format(self.id)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(NotasTarea, self).save()

    def toJSON(self):

        item = model_to_dict(self, exclude=['tareaPre','tareaPre'])
        item['user_creation'] = self.user_creation.toJSON()
        item['tareaPre'] = self.tareaPre.toJSON()
        return item

    # PARA PONER UNA IMAGEN POR default si no subieron una
    # def get_image(self):
    #    if self.imagen:
    #        return '{}{}'.format(MEDIA_URL, self.imagen)
    #    return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Notas Tarea'
        verbose_name_plural = 'Notas Tareas'
        ordering = ['id']


#TABLA INTERMEDIA


class MatriculaTarea(BaseModel):

    matri = models.ForeignKey(
        Matricula, on_delete=models.CASCADE, verbose_name='Matricula')
    
    sila = models.ForeignKey(
        Silabo, on_delete=models.CASCADE, verbose_name='Silabo')

    def _str_(self):
        return self.id

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(MatriculaTarea, self).save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['user_creation','matri','sila'])
        item['user_creation'] = self.user_creation.toJSON()
        #item['insti'] = self.insti.toJSON()
        item['matri'] = self.matri.toJSON()
        item['sila'] = self.sila.toJSON()
        #item['curso'] = [i.toJSON() for i in self.curs_set.all()]
        #item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'MatriculaTarea'
        verbose_name_plural = 'MatriculaTarea'
        ordering = ['id']
