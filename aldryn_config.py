# -*- coding: utf-8 -*-
from aldryn_client import forms
import re


class GoogleAnalyticsIDField(forms.CharField):

    GOOGLE_ANALYTICS_ID_FORMAT = re.compile(r'^UA-\d+(-\d+)?$')

    def clean(self, value):
        value = super(GoogleAnalyticsIDField, self).clean(value.strip())
        if not self.GOOGLE_ANALYTICS_ID_FORMAT.match(value):
            raise forms.ValidationError('Invalid format. Google Analytics site tracking ID format is: UA-XXXXXX-YY.')
        return value


class Form(forms.BaseForm):
    google_analytics_id = GoogleAnalyticsIDField('Tracking ID', max_length=50)

    def clean(self):
        super(Form, self).clean()
        
    def to_settings(self, data, settings):
        settings['GOOGLE_ANALYTICS_ID'] = data['google_analytics_id']
        settings['INSTALLED_APPS'].append('aldryn_google_analytics')

        # aldryn-snake is configured by aldryn-django-cms
        return settings
