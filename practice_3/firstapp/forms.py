from django import forms
import datetime

class ExampleFrom(forms.Form):
    First_name=forms.CharField(max_length=30)
    Last_name=forms.CharField(max_length=30)
    email=forms.EmailField(label="Please Enter Your Email Address..")
    birth_day=forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    TodayDate=forms.DateTimeField(initial=datetime.date.today)

    favourite_color={
        'blue':'Blue',
        'green':'Green',
        'black':'Black',

    }
    Colour=forms.ChoiceField(choices=favourite_color)
    Chooice=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=favourite_color)
    comment=forms.CharField(widget=forms.Textarea(attrs={'row':3}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    BirthDay_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    Agree=forms.BooleanField()