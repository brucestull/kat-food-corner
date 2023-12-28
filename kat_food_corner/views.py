from django.http import HttpResponse

from kat_food_corner.settings import THE_SITE_NAME


THE_APP_NAME = "Kat Food Corner"


def index(request):
    """
    Simple function-based view to display the food list
    """
    return HttpResponse(
        f"<title>{THE_SITE_NAME} - {THE_APP_NAME}</title>"
        f"Hello, Foods! You're at the {THE_SITE_NAME} : {THE_APP_NAME} site."
    )
