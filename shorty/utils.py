'''
Utilities for shortener
'''
from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE=getattr(settings, "MAXIMUM_URL_CHARS", 7) 

AVAILABLE_CHARS=ascii_letters+digits

def create_random_code(chars=AVAILABLE_CHARS):
    """
    Creates a random strings with the predetermined size
    """
    return "".join([choice(chars) for _ in range(10)])

def create_shortened_url(model_instance):
    random_code=create_random_code()
    #Gets the model class

    model_class=model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code