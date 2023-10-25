from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import Movieform
from .models import *
from  .models import Movies


def show_details(request, id):
    movie = get_object_or_404(Movies, id=id)  # Get the movie by ID
    return render(request, 'details.html', {'movie': movie})  # Pass 'movie' as a single object


def index(request):
    movies = Movies.objects.all()

    return render(request, 'index.html', {'movie_list': movies})


def add_movies(request):
    if request.method == "POST":
        name = request.POST.get("name")
        img = request.FILES["img"]
        desc = request.POST.get("desc")
        movie = Movies(name=name, img=img, desc=desc)
        movie.save()

    return render(request, 'addmovie.html')

def update_movies(request, movie_id):
    # Retrieve the movie object by its ID
    movie = get_object_or_404(Movies, id=movie_id)

    if request.method == 'POST':

        form = Movieform(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('detail', movie_id=movie_id)  # Replace 'movie_detail' with your URL name
    else:

        form = Movieform(instance=movie)

    return render(request, 'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == "POST":
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('movieapp:index')  # Redirect to the movie list page or any other appropriate page
    return render(request, 'delete.html')