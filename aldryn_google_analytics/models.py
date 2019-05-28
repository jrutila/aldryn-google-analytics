# -*- coding: utf-8 -*-
from aldryn_snake.template_api import registry
from django.conf import settings


GOOGLE_ANALYTICS_SCRIPT = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=%(google_analytics_id)s"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '%(google_analytics_id)s');
</script>"""

def get_google_analytics_script(request):
    google_analytics_id = getattr(settings, 'GOOGLE_ANALYTICS_ID', None)

    if not google_analytics_id:
        return ''
    context = {
        'google_analytics_id': google_analytics_id,
    }
    template = GOOGLE_ANALYTICS_SCRIPT
    return template % context

registry.add_to_head(get_google_analytics_script)