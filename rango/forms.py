# from django import forms
# 2 from rango.models import Page, Category
# 3
# 4 class CategoryForm(forms.ModelForm):
# 5 name = forms.CharField(max_length=128,
# 6 help_text=
# "Please enter the category name.")
# 7 views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
# 8 likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
# 9 slug = forms.CharField(widget=forms.HiddenInput(), required=False)
# 10
# 11 # An inline class to provide additional information on the form.
# 12 class Meta:
# 13 # Provide an association between the ModelForm and a model
# 14 model = Category
# 15 fields = ('name',)
# 16
# 17 class PageForm(forms.ModelForm):
# 18 title = forms.CharField(max_length=128,
# 19 help_text=
# "Please enter the title of the page.")
# 20 url = forms.URLField(max_length=200,
# 21 help_text=
# "Please enter the URL of the page.")
# 22 views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
# 23
# 24 class Meta:
# 25 # Provide an association between the ModelForm and a model
# 26 model = Page
# 27
# 28 # What fields do we want to include in our form?
# 29 # This way we don't need every field in the model present.
# 30 # Some fields may allow NULL values; we may not want to include them.
# 31 # Here, we are hiding the foreign key.
# 32 # we can either exclude the category field from the form,
# 33 exclude = ('category',)
# 34 # or specify the fields to include (don't include the category field).
# 35 #fields = ('title', 'url', 'views')

from django import forms 
from rango.models import Page,Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")

    url = forms.URLField(max_length=200,help_text="Please enter the URL of the page")
    
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page

        exclude = ('category', )




    