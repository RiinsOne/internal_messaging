from django.contrib.sessions.middleware import SessionMiddleware
from django.shortcuts import render, HttpResponseRedirect


class CustomSessionMiddleware(SessionMiddleware):
    def set_expiry(value):
        pass

    def get_expiry_age():
        pass
