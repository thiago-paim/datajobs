import logging

from django.utils import timezone
from jobs.models import Job
from jobs.scrapers import IndeedScraper

logger = logging.getLogger(__name__)


def save_jobcards(jobcards):
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
    return created_jobs, updated_jobs


def scrape_indeed_by_query(query, location="Brasil"):
    started_at = timezone.now()
    logger.info(f"Starting scrape_indeed_by_query({query=}, {location=})")
    scraper = IndeedScraper()
    params = {"q": query, "l": location}
    url = scraper.get_query_url(params)

    parser = scraper.get_parsed_search_page(url=url)
    logger.info(f"Found {len(parser.get_jobs_count())} jobs")
    jobcards = parser.get_mosaic_provider_jobcards()
    created_jobs, updated_jobs = save_jobcards(jobcards)
    next_page_url = parser.get_next_page_url()

    while next_page_url:
        parser = scraper.get_parsed_search_page(url=next_page_url)
        jobcards = parser.get_mosaic_provider_jobcards()
        c, u = save_jobcards(jobcards)
        created_jobs += c
        updated_jobs += u
        next_page_url = parser.get_next_page_url()

    finished_at = timezone.now()
    logger.info(
        f"Finishing scrape_indeed_by_query({query=}, {location=}): {len(created_jobs)} jobs created, {len(updated_jobs)} jobs updated, {len(scraper.path)} pages scraped, took {finished_at - started_at}"
    )
    return created_jobs, updated_jobs


def scrape_indeed_list_url(url):
    # Só está retornando a primeira página
    started_at = timezone.now()
    logger.info(f"Starting scrape_indeed_list_url({url=})")
    scraper = IndeedScraper()

    parser = scraper.get_parsed_search_page(url=url)
    jobcards = parser.get_mosaic_provider_jobcards()
    created_jobs, updated_jobs = save_jobcards(jobcards)

    finished_at = timezone.now()
    logger.info(
        f"Finishing scrape_indeed_list_url({url=}): {len(created_jobs)} jobs created, {len(updated_jobs)} jobs updated, took {finished_at - started_at}"
    )
    return created_jobs, updated_jobs


# TODO: Refactor
def scrape_indeed_query(query):
    """
    Scrapes Indeed jobs for a given query.
    """
    started_at = timezone.now()
    logger.info(f"Starting scrape_indeed_query({query=})")
    scraper = IndeedScraper()
    jobs = scraper.query_jobs(query=query)

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
        f"Finishing scrape_indeed_query({query=}): {len(created)} jobs created, {len(updated)} jobs updated, took {finished_at - started_at}"
    )
    return created, updated
