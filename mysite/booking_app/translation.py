from .models import Country, Hotel, Room
from modeltranslation.translator import TranslationOptions, register


@register(Country)
class CountryTranslationsOptions(TranslationOptions):
    fields = ('country_name',)


@register(Hotel)
class MovieTranslationOptions(TranslationOptions):
    fields = ('hotel_name','hotel_address', 'description')


@register(Room)
class CountryTranslationOptions(TranslationOptions):
    fields = ('room_description',)


