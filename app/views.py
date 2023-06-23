from django.shortcuts import render

# Create your views here.
from .forms import SearchForm
from .models import Dish

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            dish_name = form.cleaned_data.get('dish_name')
            dishes = Dish.objects.filter(name__icontains=dish_name)
            context = {
                'form': form,
                'dishes': dishes
            }
            return render(request, 'search_results.html', context)
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})