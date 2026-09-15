import random
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import PlaceForm


def main_view(request):
    # Отримуємо список місць із сесії користувача або порожній список, якщо його немає
    places = request.session.get('places', [])
    random_place = None
    place_id = None

    if places:
        # Витягуємо рейтинги всіх місць, щоб використати їх як вагу для ймовірності
        weights = [int(place.get('rating', 1)) for place in places]

        # random.choices обирає елемент з урахуванням ваг. k=1 означає, що нам потрібен 1 елемент.
        random_place = random.choices(places, weights=weights, k=1)[0]

        # Знаходимо індекс (id) вибраного місця, щоб передати його в шаблон для посилання
        place_id = places.index(random_place)

    # Повертаємо згенеровану відповідь HTML
    return render(request, 'places/main.html', {'random_place': random_place, 'place_id': place_id})


def places_list_view(request):
    places = request.session.get('places', [])
    # Передаємо список у шаблон для рендерингу
    return render(request, 'places/list.html', {'places': places})


def add_place_view(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        # валідація форми
        if form.is_valid():
            # Отримуємо словник
            new_place = form.cleaned_data
            new_place['created_at'] = datetime.now().strftime("%d.%m.%Y %H:%M")
            # Отримуємо поточний список із сесії
            places = request.session.get('places', [])
            places.append(new_place)

            # Зберігаємо оновлений список назад у сесію користувача
            # отут ми придумали назву 'places'
            request.session['places'] = places

            # Робимо редирект на сторінку зі списком після успішної відправки
            # Використовуємо простір імен додатку (places) та ім'я маршруту (places_list)
            return redirect('places:places_list')
    else:
        # Якщо метод GET, повертаємо порожню форму
        form = PlaceForm()
    # Рендеримо сторінку з формою, передаючи об'єкт форми в контекст
    return render(request, 'places/add_place.html', {'form': form})


def place_detail_view(request, place_id):
    # Отримуємо список місць із сесії
    places = request.session.get('places', [])
    place = None

    # Перевіряємо, чи існує місце з таким place_id у нашому списку
    if 0 <= place_id < len(places):
        place = places[place_id]
    return render(request, 'places/detail.html', {'place': place})
