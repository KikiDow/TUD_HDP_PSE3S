from django.contrib import admin
from .models import Post, Like, ExchangeRequest, Exchange

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(ExchangeRequest)
admin.site.register(Exchange)