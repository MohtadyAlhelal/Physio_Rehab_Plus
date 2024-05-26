import sys
import os

# Add the path to your virtualenv
venv_path = '/home/mohtadyAlhelal/.virtualenvs/venv'
sys.path.append(venv_path)

# Activate the virtualenv
activate_this = os.path.join(venv_path, 'bin', 'activate_this.py')
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

from django.core.wsgi import get_wsgi_application

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Clinic.settings')

application = get_wsgi_application()
