from django.shortcuts import render, redirect
from .models import Task


def home(request):

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Task.objects.create(title=title)

        return redirect("home")

    tasks = Task.objects.all().order_by("-created_at")

    return render(request, "tasks/home.html", {"tasks": tasks})