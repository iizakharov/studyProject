from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    PIECES = 'PI'
    UNITS = 'UN'
    PACKAGING = 'PC'
    KILOGRAM = 'KG'
    KILOMETER = 'KM'
    SET = 'ST'

    UNIT_CHOICES = (
        (PIECES, 'шт'),
        (UNITS, 'ед'),
        (PACKAGING, 'упак'),
        (KILOGRAM, 'кг'),
        (KILOMETER, 'км'),
        (SET, 'набор'),
    )

    created_at = models.DateTimeField(verbose_name='Дата добавления',
                                      auto_created=True, auto_now_add=True)
    name = models.CharField(verbose_name='Название', max_length=255)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    unit = models.CharField(verbose_name='Единица измерения', max_length=2,
                            choices=UNIT_CHOICES)
    vendor = models.CharField(verbose_name='Поставщик', max_length=255)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    def __str__(self):
        return self.name

