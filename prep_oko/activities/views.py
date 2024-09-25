from django.views import View
from django.shortcuts import render


class ActivitiesView(View):
    def get(self, request):
        return render(request, 'activities/main.html')
