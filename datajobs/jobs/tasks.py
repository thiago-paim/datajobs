from jobs.scrapers import IndeedScraper
from jobs.models import Job


def scrape_indeed_query(q):
    """
    Scrapes Indeed jobs for a given query.
    """

    scraper = IndeedScraper(q=q)
    jobs = scraper.run()

    for job in jobs:
        job, created = Job.objects.get_or_create(url=job["url"], defaults=job)
        if not created:
            job.title = job["title"]
            job.apply_url = job["apply_url"]
            job.description = job["description"]
            job.company_info = job["company_info"]
            job.benefits = job["benefits"]
            job.save()
