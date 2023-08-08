from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Import models here
from .models import Comic
from .forms import ReadingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def comics_index(request):
  comics = Comic.objects.all()
  return render(request, 'comics/index.html', {
    'comics': comics
  })

def comics_detail(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    reading_form = ReadingForm()
    return render(request, "comics/detail.html", {"comic": comic, "reading_form": reading_form})

def add_reading(request, comic_id):
  # create a ModelForm instance using the data in request.POST
  form = ReadingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_reading = form.save(commit=False)
    new_reading.comic_id = comic_id
    new_reading.save()
  return redirect('detail', comic_id=comic_id)

# Class Based View index
class ComicList(ListView):
    model = Comic

# CBV for Create
class ComicCreate(CreateView):
    model = Comic
    fields = ["name", "date", "description", "writer", "penciler"]

class ComicUpdate(UpdateView):
    model = Comic
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ["date", "description", "writer", "penciler"]

class ComicDelete(DeleteView):
    model = Comic
    success_url = "/comics"