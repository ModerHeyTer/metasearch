from django.shortcuts import render
# import voice_search

# Create your views here.


def index(request):
    return render(request, 'search/index.html')

# @register
# def speach_search(url):
#     result = ''
#     while not result:
#         result = voice_search.listen()
