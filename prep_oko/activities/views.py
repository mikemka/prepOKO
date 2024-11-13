from activities.forms import NewActivityForm
from activities.models import Activity
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.decorators import method_decorator
from users.models import Employee


class ActivitiesView(View):
    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self, request, **kwargs):
        students_form = kwargs.get('form_id')
        employee = Employee.objects.prefetch_related('students_forms').get(user=request.user)
        if students_form is not None:
            students_form = get_object_or_404(employee.students_forms, id=students_form)
        else:
            students_form = employee.students_forms.order_by('id').first()
        return render(request, 'activities/main.html', {
            'activities': Activity.objects.filter(user=request.user, form=students_form.title),
            'employee': employee,
            'students_form': students_form,
        })


class NewActivityView(View):
    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self, request, form_id: int):
        employee = Employee.objects.prefetch_related('students_forms').get(user=request.user)
        form = NewActivityForm()
        students_form = get_object_or_404(employee.students_forms, id=form_id)
        return render(request, 'activities/new.html', {
            'form': form,
            'employee': employee,
            'students_form': students_form,
        })

    def post(self, request, form_id: int):
        employee = Employee.objects.prefetch_related('students_forms').get(user=request.user)
        students_form = get_object_or_404(employee.students_forms, id=form_id)
        
        updated_request = request.POST.copy()
        updated_request.update({'form': [students_form.title]})
        
        form = NewActivityForm(updated_request)
        form.request = request
        if form.is_valid():
            form.save()
            return redirect('activities:main')
        
        return render(request, 'activities/new.html', {
            'form': form,
            'employee': employee,
            'students_form': students_form,
        })
