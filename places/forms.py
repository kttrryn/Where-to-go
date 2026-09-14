from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(label='Назва місця', max_length=200)
    # widget=forms.Textarea щоб було велике поле вводу
    description = forms.CharField(label='Опис', max_length=1000, widget=forms.Textarea)
    place_type = forms.CharField(label='Тип місця', max_length=100)
    location = forms.CharField(label='Локація', max_length=255, required=False)
    rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)
