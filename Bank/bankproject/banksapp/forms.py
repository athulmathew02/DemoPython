from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField()
    dob = forms.DateField()

class RegistrationForm1(forms.Form):
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')])

class RegistrationForm2(forms.Form):
    phone_number = forms.CharField()
    email = forms.EmailField()

class RegistrationForm3(forms.Form):
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ChoiceField(choices=[('trivandrum', 'Trivandrum'), ('ernakulam', 'Ernakulam'), ('alappuzha','Alappuzha'), ('thrissur', 'Thrissur'), ('kollam', 'Kollam')])

class RegistrationForm4(forms.Form):
    branch = forms.ChoiceField(choices=[('Atingal', 'Varkkala', 'Neyyattinkara'),('Angamaly', 'Perumbavoor', 'Vytilla'),('Cherthala','Chengannur','Danapady'),('Kunnamkulam', 'Kodugallur', 'Wadakkanchery'),('Anchal','Chavara','Bharanikavu')])
    account_type = forms.ChoiceField(choices=[('savings', 'Savings'), ('current', 'Current')])

class RegistrationForm5(forms.Form):
    materials_required = forms.MultipleChoiceField(choices=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('cheque', 'Chequebook')], widget=forms.CheckboxSelectMultiple)

