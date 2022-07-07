from django import forms
from .models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('ip_adress' , 'port', 'resource')
        labels = {
            'ip_adress': 'IP адрес',
            'port': 'Порт',
            'resource': 'Ресурс'
        }
