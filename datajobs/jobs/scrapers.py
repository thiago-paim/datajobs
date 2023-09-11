from django.utils import timezone
import logging
import time
import traceback
from typing import List, Dict, Optional, Tuple
import undetected_chromedriver as uc

from jobs.parsers import IndeedJobsListParser, IndeedJobParser


logger = logging.getLogger(__name__)


class BaseScraper:
    interval: int = 5
    path: List = []
    base_url: str = ""

    def get_page(self, url: str) -> str:
        """Uses undetected Chrome driver to get a page HTML."""
        logger.info(f"BaseScraper.get_page({url=})")
        url = self.base_url + url
        self.path.append(url)
        driver = uc.Chrome(headless=True, use_subprocess=False)

        try:
            driver.get(url)
            page_source: str = driver.page_source
        except Exception as exc:
            tb = traceback.format_exc()
            logger.error(f"BaseScraper.get_page({url=}: {exc}:\n{tb}")
            raise exc

        if self.interval:
            time.sleep(self.interval)

        driver.quit()
        return page_source


class IndeedScraper(BaseScraper):
    """Realiza raspagem das vagas encontradas a partir de uma busca na Indeed."""

    base_url = "https://br.indeed.com"
    search_page_address = "/jobs"
    job_page_address = "/viewjob"

    def format_url_params(self, params: dict) -> str:
        if not params:
            return ""
        return "?" + "&".join([f"{k}={v}" for k, v in params.items()])

    def get_job_url(self, jk: str) -> str:
        params = {
            "jk": jk,
        }
        return self.job_page_address + self.format_url_params(params)

    def get_query_url(self, params: dict) -> str:
        return self.search_page_address + self.format_url_params(params)

    # def get_page(self, url):
    #     """Uses undetected Chrome driver to get a page HTML."""
    #     logger.info(f"IndeedScraper.get_page({url=})")
    #     url = self.base_url + url
    #     self.path.append(url)
    #     driver = uc.Chrome(headless=True, use_subprocess=False)

    #     try:
    #         driver.get(url)
    #         page_source = driver.page_source
    #     except Exception as exc:
    #         tb = traceback.format_exc()
    #         logger.error(f"IndeedScraper.get_page({url=}: {exc}:\n{tb}")
    #         raise exc

    #     if self.interval:
    #         time.sleep(self.interval)

    #     driver.quit()
    #     return page_source

    def get_parsed_search_page(self, url: str) -> IndeedJobsListParser:
        page_source = self.get_page(url)
        return IndeedJobsListParser(page_source)

    # TODO: Refactor to return parsed page
    def get_job_details(self, jk: str) -> str:
        """Returns the HTML of a job details page."""
        url = self.get_job_url(jk)
        return self.get_page(url)

    # TODO: Refactor this method
    def query_jobs(self, q: str, l: Optional[str] = "Brasil") -> List[Dict]:
        """Executes a query and returns the jobs found (across all pages)."""
        params = {
            "q": q,
            "l": l,
        }
        jobs: List[Dict] = []

        url = self.get_query_url(params)
        jobs, n = self.search_jobs_by_url(url)

        while n:
            j, n = self.search_jobs_by_url(n)
            jobs += j

        return jobs

    # TODO: Refactor this method
    def search_jobs_by_url(self, url: str) -> Tuple[List, Optional[str]]:
        """Return the jobs found in a given search page URL."""
        started_at = timezone.now()
        logger.info(f"Starting IndeedScraper.search_jobs_by_url({url=})")
        page_source = self.get_page(url)
        parser = IndeedJobsListParser(page_source)

        job_cards = parser.get_job_cards()
        logger.info(f"Found {len(job_cards)} job cards")

        jobs = []
        for card in job_cards:
            source = self.get_job_details(card["data-jk"])
            job_page = IndeedJobParser(source)
            job = job_page.get_job()
            logger.info(f"Found job: {job['title']}")
            jobs.append(job)

        n = parser.get_next_page_url()

        finished_at = timezone.now()
        logger.info(
            f"Finishing IndeedScraper.search_jobs_by_url({url=}): {len(jobs)} jobs found, took {finished_at - started_at}"
        )
        return jobs, n
