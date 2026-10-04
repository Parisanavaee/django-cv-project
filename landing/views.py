from django.shortcuts import render
from .form import ContactForm

def index(req):
    if req.method == "POST":
        form = ContactForm(req.POST)
        try:
            if form.is_valid():
                form.save()
        except:
            return render(req, "index.html", {"form": ContactForm})
    return render(req, "index.html", {"form": ContactForm})
