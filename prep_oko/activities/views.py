from activities.forms import NewActivityForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator


class ActivitiesView(View):
    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self, request):
        return render(request, 'activities/main.html', {
            'activities': [
                {
                    'activity_type': 'Классный час',
                    'title': 'Классный час 02.05.2024',
                    'id': 12,
                    'status': 'accepted',
                },
                {
                    'activity_type': 'Внеурочная деятельность',
                    'title': 'Прогулка 02.05.2024',
                    'id': 12,
                    'status': 'rejected',
                },
                {
                    'activity_type': 'Внеурочная деятельность',
                    'title': 'Поход в кино 03.05.2024',
                    'id': 12,
                    'status': 'processing',
                },
            ]
        })


class NewActivityView(View):
    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self, request):
        form = NewActivityForm()
        return render(request, 'activities/new.html', {'form': form})

    def post(self, request):
        form = NewActivityForm(request.POST)
        form.request = request
        if form.is_valid():
            form.save()
            return redirect('activities:main')
        return render(request, 'activities/new.html', {'form': form})
