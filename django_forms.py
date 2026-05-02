from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label="Ім'я")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Повідомлення")

    def clean_name(self):
        name = self.cleaned_data["name"]
        if "@" in name:
            raise forms.ValidationError("Ім'я не може містити @")
        return name
