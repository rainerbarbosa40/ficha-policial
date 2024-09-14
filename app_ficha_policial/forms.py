from django import forms
from .models import FichaPolicial

class FichaPolicialForm(forms.ModelForm):
    class Meta:
        model = FichaPolicial
        fields = '__all__'  # Ou especifique os campos que deseja incluir

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-sm'})
