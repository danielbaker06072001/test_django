from django import forms 

from .models import Product 
 

class ProductForm(forms.ModelForm): 
    title       = forms.CharField(label = '', widget = forms.TextInput(attrs={
                                                            "placeholder": "your title"})) 
    email = forms.EmailField()
    description = forms.CharField(
                                required = True, 
                                widget = forms.Textarea(
                                    attrs = { 
                                        "placeholder" : "title" ,
                                        "class" : "new-class-name two", 
                                        "id" : "my-id-for-textares",
                                        "rows" : 20,
                                        "cols" : 120
                                        }
                                    )
                                ) 
    price = forms.DecimalField(initial = 199.99) 

    class Meta : 
        model = Product 
        fields = [
            'title', 
            'description', 
            'price'
        ]


    def clean_title(self, *args, **kwargs): 
        title = self.clean_data.get("title") 
        if not "CFE" in title : 
            raise forms.ValidationError("This is not valid")
        if not "news" in title: 
            raise forms.ValidationError("this is not a valid")
        return title

    def clean_email(self, *args, **kwargs): 
        email = self.clean_data.get("email") 
        if not email.endswith("edu") :
            raise forms.ValidationError("This is not a valid email")
        
        return email


class RawProductForm(forms.Form) : 
    title       = forms.CharField(label = '', widget = forms.TextInput(attrs={
                                                            "placeholder": "your title"})) 
    description = forms.CharField(
                                required = True, 
                                widget = forms.Textarea(
                                    attrs = { 
                                        "placeholder" : "title" ,
                                        "class" : "new-class-name two", 
                                        "id" : "my-id-for-textares",
                                        "rows" : 20,
                                        "cols" : 120
                                        }
                                    )
                                ) 
    price = forms.DecimalField(initial = 199.99) 