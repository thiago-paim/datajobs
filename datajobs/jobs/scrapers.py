from django.utils import timezone
import logging
import time
import undetected_chromedriver as uc

from jobs import parsers


logger = logging.getLogger(__name__)


class IndeedScraper:
    """Realiza raspagem das vagas encontradas a partir de uma busca na Indeed."""

    domain = "https://br.indeed.com"
    search_page_address = "/jobs?"
    job_page_address = "/viewjob?"
    path = []
    interval = 5

    def build_job_url(self, jk):
        return self.job_page_address + "jk=" + jk

    def build_search_url(self, params):
        url_params = "&".join([f"{k}={v}" for k, v in params.items()])
        return self.search_page_address + url_params

    def get_page(self, url):
        """Uses undetected Chrome driver to get a page HTML."""
        logger.info(f"IndeedScraper.get_page({url=})")
        url = self.domain + url
        driver = uc.Chrome(headless=True, use_subprocess=False)
        driver.get(url)
        page_source = driver.page_source
        if self.interval:
            time.sleep(self.interval)
        driver.quit()
        self.path.append(url)
        return page_source

    def get_job_details(self, jk):
        """Returns the HTML of a job details page."""
        url = self.build_job_url(jk)
        return self.get_page(url)

    def query_jobs(self, q, l="Brasil"):
        """Executes a query and returns the jobs found (across all pages)."""
        params = {
            "q": q,
            "l": l,
        }
        url = self.build_search_url(params)
        jobs, next = self.search_jobs_by_url(url)

        while next:
            j, next = self.search_jobs_by_url(next)
            jobs += j

        return jobs

    def search_jobs_by_url(self, url):
        """Return the jobs found in a given search page URL."""
        started_at = timezone.now()
        logger.info(f"Starting IndeedScraper.search_jobs_by_url({url=})")
        page_source = self.get_page(url)
        page = parsers.IndeedJobsListParser(page_source)

        job_cards = page.get_job_cards()
        logger.info(f"Found {len(job_cards)} job cards")

        jobs = []
        for card in job_cards:
            source = self.get_job_details(card["data-jk"])
            job_page = parsers.IndeedJobParser(source)
            job = job_page.get_job()
            logger.info(f"Found job: {job['title']}")
            jobs.append(job)

        next = page.get_next_page_url()

        finished_at = timezone.now()
        logger.info(
            f"Finishing IndeedScraper.search_jobs_by_url({url=}): {len(jobs)} jobs found, took {finished_at - started_at}"
        )
        return jobs, next
