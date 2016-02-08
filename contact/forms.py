from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    name = forms.CharField(label='Full Names', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Names'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}))
    cc_myself = forms.BooleanField(required=False)