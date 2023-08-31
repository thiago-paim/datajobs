import logging
from selenium.webdriver.chrome.options import Options
import time
import undetected_chromedriver as uc

from jobs import parsers


logger = logging.getLogger(__name__)


class IndeedScraper:
    """Realiza raspagem das vagas encontradas a partir de uma busca na Indeed."""

    domain = "https://br.indeed.com"
    job_path = "/jobs"
    interval = 2
    chrome_version = 116

    def __init__(self, q, l="Brasil", headless=True):
        logger.info(f"Creating IndeedScraper with: q={q}, l={l} headless={headless}")
        self.params = {
            "q": q,
            "l": l,
        }
        self.url = self.build_url()

        self.options = Options()
        self.options.add_argument("--incognito")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-application-cache")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--remote-debugging-port=9222")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-setuid-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        if headless:
            self.options.add_argument("--headless=new")

        self.driver = uc.Chrome(options=self.options, version_main=self.chrome_version)

    def build_url(self):
        params = "&".join([f"{k}={v}" for k, v in self.params.items()])
        return self.domain + self.job_path + "?" + params

    def run(self):
        logger.info(f"Running IndeedScraper with url={self.url}")
        self.driver.get(self.url)

        self.results_page = self.driver.page_source
        parsed_results = parsers.IndeedJobsListParser(self.results_page)
        self.cards = parsed_results.get_job_cards()
        logger.info(f"Found {len(self.cards)} job cards")

        self.jobs = []
        for card in self.cards:
            job_url = self.domain + card["href"]
            logger.info(f"Scraping job from url={job_url}")
            if self.interval:
                time.sleep(self.interval)

            try:
                self.driver.get(job_url)
                parser = parsers.IndeedJobParser(self.driver.page_source)

                job = parser.get_job()
                self.jobs.append(job)
            except Exception as e:
                logger.error(f"Error parsing job: {e}\njob_url={job_url}")

        return self.jobs
