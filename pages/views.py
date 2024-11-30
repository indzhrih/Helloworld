from django.http import HttpResponse

def homePageViews(reguest):
    return  HttpResponse('Anya the best')
