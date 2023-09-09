from django.core.management.base import BaseCommand
from jobs.models import Job
from jobs.tasks import scrape_indeed_by_query
from jobs.utils import export
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Scrape Indeed jobs for a given query and location"

    def add_arguments(self, parser):
        parser.add_argument("q", type=str)
        parser.add_argument("l", type=str)

    def handle(self, *args, **options):
        q = options["q"]
        l = options["l"]
        logger.info(f"Scraping Indeed jobs for {q=} and {l=}")

        created, updated = scrape_indeed_by_query(q, l)
        job_ids = [job.id for job in created + updated]
        jobs = Job.objects.filter(id__in=job_ids)
        logger.info(f"Found {len(jobs)} jobs")

        filename = f"q={q}&l={l}"
        filepath = export(jobs, filename=filename)
        logger.info(f"Jobs exported to {filepath}")
