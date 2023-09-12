import pandas as pd
from django.conf import settings
from django.utils import timezone


def export(queryset, filename=None):
    if not filename:
        filename = f"{queryset.model.__name__.lower()}s"

    time_signature = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    filepath = f"{settings.DEFAULT_EXPORT_PATH}{time_signature} {filename}.csv"
    df = pd.DataFrame(job.to_dict() for job in queryset)

    chunksize = 1000
    df.to_csv(filepath, chunksize=chunksize, sep=";")

    return filepath
