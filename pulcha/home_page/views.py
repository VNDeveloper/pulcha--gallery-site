from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    if request.user.is_authenticated:
        template_name = 'home/home.html'

    return render(request, template_name, {})
