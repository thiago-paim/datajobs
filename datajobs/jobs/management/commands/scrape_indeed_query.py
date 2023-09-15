import logging

from django.core.management.base import BaseCommand
from jobs.models import Job
from jobs.tasks import scrape_indeed_by_query
from jobs.utils import export

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Scrape Indeed jobs for a given query and location"

    def add_arguments(self, parser):
        parser.add_argument("query", type=str)
        parser.add_argument("location", type=str)

    def handle(self, *args, **options):
        query = options["query"]
        location = options["location"]
        logger.info(f"Scraping Indeed jobs for {query=} and {location=}")

        created, updated = scrape_indeed_by_query(query, location)
        job_ids = [job.id for job in created + updated]
        jobs = Job.objects.filter(id__in=job_ids)
        logger.info(f"Found {len(jobs)} jobs")

        filename = f"q={query}&l={location}"
        filepath = export(jobs, filename=filename)
        logger.info(f"Jobs exported to {filepath}")
