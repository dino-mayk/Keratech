from django.shortcuts import redirect

from Keratech.settings import DOMEN


class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/' or request.path.startswith('/www.'):
            return redirect(f'https://{DOMEN}/')
        response = self.get_response(request)
        return response
