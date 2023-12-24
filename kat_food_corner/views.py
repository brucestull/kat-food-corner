from django.http import HttpResponse

from kat_food_corner.settings import THE_SITE_NAME


def index(request):
    """
    Simple function-based view to display the food list
    """
    return HttpResponse(f"Hello, Foods! You're at the {THE_SITE_NAME} site.")
