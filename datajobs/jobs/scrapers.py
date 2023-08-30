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

        self.driver = uc.Chrome(options=self.options)

    def build_url(self):
        params = "&".join([f"{k}={v}" for k, v in self.params.items()])
        return self.domain + self.job_path + "?" + params

    def run(self):
        self.driver.get(self.url)

        self.results_page = self.driver.page_source
        parsed_results = parsers.IndeedJobsListParser(self.results_page)
        self.cards = parsed_results.get_job_cards()

        self.jobs = []
        for card in self.cards:
            job_url = self.domain + card["href"]
            if self.interval:
                time.sleep(self.interval)

            try:
                self.driver.get(job_url)
                parser = parsers.IndeedJobParser(self.driver.page_source)

                job = parser.get_job()
                self.jobs.append(job)
            except Exception as e:
                print(f"Error parsing job: {e}\njob_url={job_url}")

        return self.jobs
