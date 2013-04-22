# -*- coding: utf-8 -*-
from cmscloud_client import forms


class Form(forms.BaseForm):

    google_analytics_id = forms.CharField('Tracking ID', max_length=50)

    def to_settings(self, data, settings):
        settings['GOOGLE_ANALYTICS_ID'] = data['google_analytics_id']
        return settings
