import sys
import os


from django.core.wsgi import get_wsgi_application

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Clinic.settings')

application = get_wsgi_application()
