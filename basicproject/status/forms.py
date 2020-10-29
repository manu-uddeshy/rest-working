from django import forms
from django.forms import fields
from .models import Status

#create your froms here
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields  = [
            'user',
            'content',
            'image'
        ]
    
    def clean(self):
        #data = self.cleaned_data()
        super(StatusForm,self).clean() 
        content = self.cleaned_data.get('content',None)
        if content == "":
            content = None
        image = self.cleaned_data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('content or image is required!')
        return self.cleaned_data