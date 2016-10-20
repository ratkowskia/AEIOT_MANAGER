from django import forms
from .models import Supplier, Consumer, DataFormat


class AlgorithmDetailsForm(forms.Form):
    #algorithm_id = forms.HiddenInput()
    name = forms.CharField(max_length=100, required=False)
    semantics = forms.CharField(max_length=100, required=False)
    source_code = forms.CharField(widget=forms.Textarea, required=False)
    version = forms.EmailField(required=False)
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)
    input_format = forms.ModelChoiceField(queryset=DataFormat.objects.all(), required=False)
    output_format = forms.ModelChoiceField(queryset=DataFormat.objects.all(), required=False)


    def save(self):
        return





class ProfileForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    as_supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)
    as_consumer = forms.ModelChoiceField(queryset=Consumer.objects.all(), required=False)


    def save(self):
        return


class AlgorithmSearch(forms.Form):
    search_phrase = forms.CharField(max_length=100, required=False)

    def save(self):
        return

