from .models import User, Doctor
from modeltranslation.translator import TranslationOptions, register


@register(Doctor)
class CarTranslationOptions(TranslationOptions):
    fields = ("specialty",)