from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, "home.html", {"title": "Головна", "number": 5})

def form_view(request):
    if request.method == "POST":
        name = request.POST.get("name")

        if not name:
            messages.error(request, "Ім'я обов'язкове!")
        else:
            messages.success(request, "Успішно відправлено!")

        return redirect("form")

    return render(request, "form.html")
