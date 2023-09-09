from django.core.management.base import BaseCommand
from jobs.models import Job
from jobs.tasks import scrape_indeed_list_url
from jobs.utils import export
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Scrape Indeed jobs for a given URL"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str)

    def handle(self, *args, **options):
        url = options["url"]
        logger.info(f"Scraping Indeed jobs on {url=}")

        created, updated = scrape_indeed_list_url(url)
        job_ids = [job.id for job in created + updated]
        jobs = Job.objects.filter(id__in=job_ids)
        logger.info(f"Found {len(jobs)} jobs")

        filepath = export(jobs)
        logger.info(f"Jobs exported to {filepath}")
