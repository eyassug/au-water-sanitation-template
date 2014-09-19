import os, sys
sys.path.append('c"\\xammp\\htdocs\\auwsssp')
os.environ['DJANGO_SETTINGS_MODULE']='auwsssp.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()