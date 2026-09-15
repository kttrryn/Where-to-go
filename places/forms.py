from django import forms

PLACE_TYPES = [
    ('cafe', 'Кафе'),
    ('park', 'Парк'),
    ('restaurant', 'Ресторан'),
    ('bar', 'Бар'),
    ('cinema', 'Кінотеатр'),
    ('bookstore', 'Книгарня/бібліотека'),
    ('museum', 'Музей'),
    ('other', 'Інше'),
]


class PlaceForm(forms.Form):
    name = forms.CharField(label='Назва місця', max_length=200)
    # widget=forms.Textarea щоб було велике поле вводу
    description = forms.CharField(label='Опис', max_length=255, widget=forms.Textarea)
    place_type = forms.ChoiceField(label='Тип місця', choices=PLACE_TYPES)
    location = forms.CharField(label='Локація', max_length=255, required=False)
    rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)
