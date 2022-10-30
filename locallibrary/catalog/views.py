from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Book, Author, BookInstance, Genre
from . import constants
from django.views import generic


# Create your views here.
def index(request):
  """View function for home page of site."""

  # Generate counts of some of the main objects
  num_books = Book.objects.count()

  num_instances = BookInstance.objects.count()

  # Available books (status = 'a')
  num_instances_available = BookInstance.objects.filter(status__exact=constants.BOOK_STATUS_AVAILABLE).count()

  # The 'all()' is implied by default.
  num_authors = Author.objects.count()

  num_genres = Genre.objects.filter(name__exact= constants.GENRE_NAME).count()

  context = {
      'num_books': num_books,
      'num_instances': num_instances,
      'num_instances_available': num_instances_available,
      'num_authors': num_authors,
      'num_genres': num_genres
  }

  # Render the HTML template index.html with the data in the context variable
  return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
  model = Book
  paginate_by = 1

class AuthorListView(generic.ListView):
  model = Author

class BookDetailView(generic.DetailView):
  model = Book

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["book_genres"] = context["book"].genre.all()
    context["book_instances"] = context["book"].bookinstance_set.all()
    return context

class AuthorDetailView(generic.DetailView):
  model = Author
