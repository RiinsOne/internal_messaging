from django.contrib.sessions.middleware import SessionMiddleware
from django.shortcuts import render, HttpResponseRedirect


class CustomSessionMiddleware(SessionMiddleware):
    def set_expiry(value):
        pass

    def get_expiry_age():
        pass


# class AuthRequiredMiddleware(object):
#     def process_request(self, request):
#         if not request.user.is_authenticated():
#             return HttpResponseRedirect(reverse('login')) # or http response
#         return None
