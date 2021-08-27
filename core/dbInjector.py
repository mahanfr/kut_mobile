import json
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from announcement.models import Announcement

