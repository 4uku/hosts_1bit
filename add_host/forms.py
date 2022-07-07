from django import forms

from .models import Host


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('ip_adress', 'port', 'resource')
        labels = {
            'ip_adress': 'IP адрес',
            'port': 'Порт',
            'resource': 'Ресурс'
        }


class HostFormAdmin(HostForm):
    class Meta:
        model = Host
        fields = ('ip_adress', 'port', 'resource', 'owners')
        labels = {
            'ip_adress': 'IP адрес',
            'port': 'Порт',
            'resource': 'Ресурс',
            'owners': 'Владельцы'
        }
