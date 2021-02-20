from datetime import datetime
from django.forms import *
from core.erp.models import Category,Curso,Deber,NotasTarea, SubirTarea, Instituto, Matricula, Silabo,Profesor,Materia,Alumno

class CategoryForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Category
        fields = '__all__'
        
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder':'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder':'Descriptions',
                    'rows':3,
                    'cols':3
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned


class InstitutoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Instituto
        fields = '__all__'
        
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder':'Ingrese un nombre',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder':'Ingrese la Direccion',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder':'Ingrese el telefono',
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder':'Ingrese un correo Electronico',
                }
            ),
        }
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned


class MatriculaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['periodo'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'fecha': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'periodo': Select(
               
            ),
            'insti': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class SilaboForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['titulo'].widget.attrs['autofocus'] = True
    class Meta:
        model = Silabo
        fields = '__all__'
        
        widgets = {
            'titulo': TextInput(
                attrs={
                    'placeholder':'Ingrese el Titulo de la tarea',
                }
            ),
            
            'Descripcion': Textarea(
                attrs={
                    'placeholder':'Descripcion de la Tarea',
                    'rows':3,
                    'cols':3
                }
            ),
            'document': FileInput(
                attrs={
                    'name':'pdf',
                    'accept':'application/pdf'
                }
            ),
            
        }
        exclude = ['user_updated', 'user_creation']
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned

class ProfesorForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Profesor
        fields = '__all__'
        
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder':'Ingrese el nombre',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder':'Ingrese el Apellido',
                }
            ),
            'especialid': TextInput(
                attrs={
                    'placeholder':'Ingrese la Especialidad',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder':'Ingrese el telefono',
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder':'Ingrese el Correo Electronico',
                }
            ),            
        }
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned

class MateriaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Materia
        fields = '__all__'
        
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder':'Ingrese el nombre',
                }
            )
        }
        exclude = ['user_updated', 'user_creation']
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned



class AlumnoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Alumno
        fields = '__all__'
        
        widgets = {
            'cedula': TextInput(
                attrs={
                    'placeholder':'Ingrese el nombre',
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder':'Ingrese el nombre',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder':'Ingrese el Apellido',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder':'Ingrese la Especialidad',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder':'Ingrese el telefono',
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder':'Ingrese el Correo Electronico',
                }
            ),            
        }
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned


class DeberForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['titulo'].widget.attrs['autofocus'] = True
    class Meta:
        model = Deber
        fields = '__all__'
        
        widgets = {
            'tema': TextInput(
                attrs={
                    'placeholder':'Ingrese el Tema de la tarea',
                }
            ),
            'document': FileInput(
                attrs={
                    'name':'pdf',
                    'accept':'application/pdf'
                }
            ),            
            
        }
        exclude = ['user_updated', 'user_creation']
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned



class SubirTareaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['titulo'].widget.attrs['autofocus'] = True
    class Meta:
        model = SubirTarea
        fields = '__all__'
        
        widgets = {

            'tarea': FileInput(
                attrs={
                    'name':'pdf',
                    'accept':'application/pdf'
                }
            ),
            
        }
        exclude = ['user_updated', 'user_creation']
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned


class NotasTareaForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['titulo'].widget.attrs['autofocus'] = True
    class Meta:
        model = NotasTarea
        fields = '__all__'
        
        widgets = {
            'tareaPre': Select(),
            'nota': TextInput(
                attrs={
                    'placeholder':'Ingrese la nota',
                }
            ),
            'observacion': Textarea(
                attrs={
                    'placeholder':'Observaciones',
                }
            ),
            
        }
        exclude = ['user_updated', 'user_creation']
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned




class CursoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            #form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['titulo'].widget.attrs['autofocus'] = True
    class Meta:
        model = Curso
        fields = '__all__'
        
        widgets = {
            'nivel': TextInput(
                attrs={
                    'placeholder':'Ingrese el Nivel',
                }
            ),
            'Paralelo': Select(),
            'mate': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple'
            }),
        }
        exclude = ['user_updated', 'user_creation']
    def save(self, commit= True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    #VALIDACIONES EXTRAS    
    #def clean (self):
    #    cleaned = super().clean()
    #    if len(cleaned['nombre']) <- 50:
    #        raise forms.ValidationError('Validacion xx')
    #        
    #        #self.add_error('nombre','Le faltan caracteres')
    #    print(cleaned)
    #    return cleaned

