from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from bookapp.forms import BookForm
from bookapp.models import Book

from django.db.models.functions import Lower
from django.db.models import Avg, Count, Max, Min

# Create your views here.
class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/form.html'
    success_url = reverse_lazy('book_list')

class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'bookapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(title__icontains=query) 

        sort = self.request.GET.get("sort", "title")
        
        if sort in ["title", "pages", "rating", "status", "published_date"]:
            queryset = queryset.order_by(Lower(sort))
            
        return queryset

class BookUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'bookapp.change_book'
    model = Book
    form_class = BookForm
    template_name = 'bookapp/form.html'
    success_url = reverse_lazy('book_list')

class BookDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'bookapp.delete_book'
    model = Book
    template_name = 'bookapp/confirm_delete.html'
    success_url = reverse_lazy('book_list')

class BookDetail(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'bookapp/detail.html'
    context_object_name = 'book'

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('book_list')
    return render(request, 'bookapp/form.html', {'form': form})

def book_stats(request):
    stats = Book.objects.aggregate(
        max_pages=Max('pages'),
        min_pages=Min('pages'),
        avg_pages=Avg('pages'),
        avg_rating=Avg('rating')
    )

    by_status = Book.objects.values("status").annotate(total=Count("id"))

    by_rating = Book.objects.values("rating").annotate(total=Count("id")).order_by("rating")

    return render(request, "bookapp/stats.html", {
        "stats": stats,
        "status_labels": [s['status'] for s in by_status],
        "status_counts": [s['total'] for s in by_status],
        "rating_labels": [str(r['rating']) for r in by_rating],
        "rating_counts": [r['total'] for r in by_rating],
    })