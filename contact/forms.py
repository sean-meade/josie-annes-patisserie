from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), label='')
