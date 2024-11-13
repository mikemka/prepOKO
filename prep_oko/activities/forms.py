from activities.models import Activity, ActivityType, LevelType
from django import forms

class NewActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('activity_type', 'level_type', 'title', 'description', 'form')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['activity_type'].queryset = ActivityType.objects.all()
        self.fields['level_type'].queryset = LevelType.objects.all()
        self.fields['form'].widget = forms.HiddenInput()

    def save(self, commit=True):
        activity = super().save(commit=False)
        activity.user = self.request.user
        if commit:
            activity.save()
        return activity
