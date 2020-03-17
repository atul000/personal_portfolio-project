from django.shortcuts import render


def all_blogs(request):
    return render(request, 'blogs/all_blogs.html')
