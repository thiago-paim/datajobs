from django.utils import timezone
import logging
from jobs.scrapers import IndeedScraper
from jobs.models import Job

logger = logging.getLogger(__name__)


def scrape_indeed_list_url(url):
    started_at = timezone.now()
    logger.info(f"Starting scrape_indeed_list_url({url=})")
    scraper = IndeedScraper()
    jobcards = scraper.get_jobcards_by_url(url=url)

    created_jobs = []
    updated_jobs = []
    for jobcard in jobcards:
        job, created = Job.objects.update_or_create(
            jobkey=jobcard["jobkey"], defaults=jobcard
        )
        if created:
            created_jobs.append(job)
        else:
            updated_jobs.append(job)

    finished_at = timezone.now()
    logger.info(
        f"Finishing scrape_indeed_list_url({url=}): {len(created_jobs)} jobs created, {len(updated_jobs)} jobs updated, took {finished_at - started_at}"
    )
    return created_jobs, updated_jobs


# TODO: Refactor
def scrape_indeed_query(q):
    """
    Scrapes Indeed jobs for a given query.
    """
    started_at = timezone.now()
    logger.info(f"Starting scrape_indeed_query({q=})")
    scraper = IndeedScraper()
    jobs = scraper.query_jobs(q=q)

    created = []
    updated = []
    for job in jobs:
        j, created = Job.objects.update_or_create(url=job["url"], defaults=job)
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
