# -*- coding: utf-8 -*-
from cmscloud.template_api import registry
from django.conf import settings

GOOGLE_ANALYTICS_SCRIPT = """<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '%(google_analytics_id)s']);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>"""


def get_google_analytics_script():
    google_analytics_id = getattr(settings, 'GOOGLE_ANALYTICS_ID', None)
    if google_analytics_id:
        return GOOGLE_ANALYTICS_SCRIPT % {'google_analytics_id': google_analytics_id}
    else:
        return ''

registry.add_to_tail(get_google_analytics_script())
