from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django homepage!")

def first(request, para):
    return HttpResponse(f"You entered: {para}")
