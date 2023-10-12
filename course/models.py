from datetime import datetime, timedelta
from typing import TYPE_CHECKING, List, Optional

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_extensions.db import models as e_models


class Course(e_models.TitleSlugDescriptionModel):
    subtitle = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.PositiveIntegerField(null=True)
