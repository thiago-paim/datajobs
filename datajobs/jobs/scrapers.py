from selenium.webdriver.chrome.options import Options
import time
import undetected_chromedriver as uc

from jobs import parsers


class IndeedScraper:
    """Realiza raspagem das vagas encontradas a partir de uma busca na Indeed."""

    domain = "https://br.indeed.com"
    job_path = "/jobs"
    interval = 2

    def __init__(self, q, l="Brasil", headless=True):
        self.params = {
            "q": q,
            "l": l,
        }
        self.url = self.build_url()
        self.options = Options()
        if headless:
            self.options.add_argument("--headless=new")

    def build_url(self):
        params = "&".join([f"{k}={v}" for k, v in self.params.items()])
        return self.domain + self.job_path + "?" + params

    def run(self):
        driver = uc.Chrome(options=self.options)
        driver.get(self.url)

        self.results_page = driver.page_source
        parsed_results = parsers.IndeedJobsListParser(self.results_page)
        self.cards = parsed_results.get_job_cards()

        self.jobs = []
        for card in self.cards:
            if self.interval:
                time.sleep(self.interval)

            job_url = self.domain + card["href"]
            driver.get(job_url)
            parser = parsers.IndeedJobParser(driver.page_source)

            job = parser.get_job()
            self.jobs.append(job)

        return self.jobs
