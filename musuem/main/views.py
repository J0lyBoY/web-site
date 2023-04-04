from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def exhibition(request):
    return render(request, 'main/exhibition.html')


def panoram_view(request):
    return render(request, 'main/panoram_view.html')


def people_photos(request):
    return render(request, 'main/people_photos.html')


def exibition_photo(request):
    return render(request, 'main/exibition_photo.html')
