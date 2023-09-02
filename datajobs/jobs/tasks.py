from django.utils import timezone
import logging
from jobs.scrapers import IndeedScraper
from jobs.models import Job

logger = logging.getLogger(__name__)


def scrape_indeed_query(q):
    """
    Scrapes Indeed jobs for a given query.
    """
    started_at = timezone.now()
    logger.info(f"Starting scrape_indeed_query({q=})")
    scraper = IndeedScraper()
    jobs = scraper.search_jobs(q=q)

    created = []
    updated = []
    for job in jobs:
        j, created = Job.objects.get_or_create(url=job["url"], defaults=job)
        if not created:
            j.title = job["title"]
            j.apply_url = job["apply_url"]
            j.description = job["description"]
            j.company_info = job["company_info"]
            j.benefits = job["benefits"]
            j.save()
            updated.append(j)
        else:
            created.append(j)

    finished_at = timezone.now()
    logger.info(
        f"Finishing scrape_indeed_query({q=}): {len(created)} jobs created, {len(updated)} jobs updated, took {finished_at - started_at}"
    )
    return created, updated
