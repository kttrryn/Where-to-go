from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(max_length=1000, verbose_name="Опис")
    place_type = models.CharField(max_length=100, verbose_name="Тип місця")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Локація")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рейтинг"
    )

    # auto_now_add=True ставить поточний час при збереженні
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    # Ідентифікатор сесії для ізоляції списків між користувачами
    session_id = models.CharField(max_length=255, verbose_name="Ідентифікатор сесії")

    # цей метод вказує Django як саме називати запис з бази даних
    def __str__(self):
        return self.name
