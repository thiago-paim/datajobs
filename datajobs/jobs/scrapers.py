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
    cloudflare_title = "Just a moment..."  # For dealing with errors

    def build_search_url(self, params):
        url_params = "&".join([f"{k}={v}" for k, v in params.items()])
        return self.search_page_address + url_params

    def build_job_url(self, jk):
        return self.job_page_address + "jk=" + jk

    def get_page(self, url):
        logger.info(f"IndeedScraper.get_page({url=})")
        url = self.domain + url
        driver = uc.Chrome(headless=True, use_subprocess=False)
        driver.get(url)
        page_source = driver.page_source
        title = driver.title
        if self.interval:
            time.sleep(self.interval)
        driver.quit()
        self.path.append(url)
        return title, page_source

    def get_search_results(self, q, l="Brasil"):
        params = {
            "q": q,
            "l": l,
        }
        url = self.build_search_url(params)
        return self.get_page(url)

    def get_job_details(self, jk):
        url = self.build_job_url(jk)
        return self.get_page(url)

    def search_jobs(self, q, l="Brasil"):
        started_at = timezone.now()
        logger.info(f"Starting IndeedScraper.search_jobs({q=}, {l=})")
        _, source = self.get_search_results(q, l)

        search_page = parsers.IndeedJobsListParser(source)
        job_cards = search_page.get_job_cards()
        logger.info(f"Found {len(job_cards)} job cards")

        self.jobs = []
        for card in job_cards:
            _, source = self.get_job_details(card["data-jk"])
            job_page = parsers.IndeedJobParser(source)
            job = job_page.get_job()
            logger.info(f"Found job: {job['title']}")
            self.jobs.append(job)

        # To Do: Adicionar paginação

        finished_at = timezone.now()
        logger.info(
            f"Finishing IndeedScraper.search_jobs({q=}, {l=}): {len(self.jobs)} jobs found, took {finished_at - started_at}"
        )
        return self.jobs
