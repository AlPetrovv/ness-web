from django import forms


class DateInputForm(forms.Form):
    date = forms.DateField(
        required=True,
        label=False,
        widget=forms.DateInput(
            attrs={'type': 'date'}
        ),
    )
