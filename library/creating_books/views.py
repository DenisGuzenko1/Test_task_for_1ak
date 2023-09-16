from django.shortcuts import render, redirect

from .forms import New_book


def create(request):
    if request.method == 'POST':
        form = New_book(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('index')
    else:
        form = New_book()
    return render(request, 'create.html', {'form': form})
