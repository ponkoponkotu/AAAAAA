from django import forms
from .models import PregnantMomsHealth



class PregnantMomsCreateForm(forms.ModelForm):
    class Meta:
        model = PregnantMomsHealth
        fields = ('pregnancy_week',
                  'my_date',
                  'height',
                  'weight',
                  'blood_pressure_upper',
                  'blood_pressure_under',
                  'waist',
                  'fundall_length',
                  'edema',
                  'unrine_protein',
                  'diabetes',
                  'other_test',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
