from bs4 import BeautifulSoup
from bs4.element import Tag
import json
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class PageParser:
    def __init__(self, page: str) -> None:
        self.soup = BeautifulSoup(page, "html.parser")


class IndeedJobParser(PageParser):
    """Parser for Indeed job pages."""

    def __init__(self, page: str) -> None:
        super().__init__(page)
        self.job = self.get_job()

    def get_job(self):
        job = {
            "html": "",
            "url": "",
            "title": "",
            "company_info": "",
            "apply_url": "",
            "benefits": "",
            "description": "",
            # "salary_and_job_info": "",
        }

        # job["html"] = str(self.soup)

        url = self.soup.select("link[rel='canonical']")
        if url:
            job["url"] = url[0].attrs["href"]

        title = self.soup.select("h1 span")
        if title:
            job["title"] = title[0].string

        company_info = self.soup.select(
            "div[data-testid='jobsearch-CompanyInfoContainer']"
        )
        if company_info:
            job["company_info"] = company_info[0].get_text().strip("\n")

        # apply_button = self.soup.select("div#applyButtonLinkContainer button")
        # if apply_button:
        #     job["apply_url"] = apply_button[0].attrs["href"]

        # benefits = self.soup.select("div#benefits")
        # if benefits:
        #     job["benefits"] = str(benefits[0])

        description = self.soup.select("div#jobDescriptionText")
        if description:
            job["description"] = description[0].get_text().strip("\n")

        # salary_and_job_info = self.soup.select("div#salaryInfoAndJobType")
        # if salary_and_job_info:
        #     job["salary_and_job_info"] = str(salary_and_job_info[0])

        return job


class IndeedJobsListParser(PageParser):
    """Parser for Indeed search results pages."""

    def get_jobs_count(self) -> Optional[str]:
        count = self.soup.select("div.jobsearch-JobCountAndSortPane-jobCount")
        if count:
            return count[0].text.split(" ")[0]
        else:
            return None

    # TODO: Remove this method
    def get_job_from_card(self, card: Tag) -> Dict:
        job: Dict[str, Optional[str]] = {
            "title": None,
            "data-jk": None,
            "href": None,
            "company_name": None,
            "company_location": None,
            # "metadata": None,
            # "job_snippet": None,
            # "posted_date": None,
        }
        job["title"] = card.select("h2.jobTitle span")[0].string
        job["data-jk"] = card.select("a")[0].attrs["data-jk"]  # ID do anúncio
        job["href"] = card.select("a")[0].attrs["href"]

        company_name = card.select("span.companyName")
        if company_name:
            job["company_name"] = company_name[0].string

        company_location = card.select("div.companyLocation")
        if company_location:
            job["company_location"] = company_location[0].string

        # metadata = card.select("div.metadata")
        # if metadata:
        #     job["metadata"] = metadata[0]

        # job_snippet = card.select("div.job-snippet")
        # if job_snippet:
        #     job["job_snippet"] = job_snippet[0]

        # job["posted_date"] = card.select("table.jobCardShelfContainer span.date")[0]

        return job

    # TODO: Remove this method
    def get_job_cards(self) -> List[Dict]:
        self.jobs: List = []

        jobcards = self.soup.select("div#mosaic-provider-jobcards div.slider_container")
        for card in jobcards:
            try:
                job = self.get_job_from_card(card)
                self.jobs.append(job)
            except Exception as e:
                logger.error(f"Error parsing job card: {e}\ncard={card}")

        return self.jobs

    def get_next_page_url(self) -> Optional[str]:
        next_page = self.soup.select("link[rel='next']")
        if next_page:
            return next_page[0].attrs["href"]
        else:
            return None

    def get_previous_page_url(self) -> Optional[str]:
        prev_page = self.soup.select("link[rel='prev']")
        if prev_page:
            return prev_page[0].attrs["href"]
        else:
            return None

    def get_mosaic_provider_jobcards(self) -> Optional[List[Dict]]:
        script = self.soup.select("script#mosaic-data")
        if not script:
            return None

        line_start = 'providerData["mosaic-provider-jobcards"]'
        lines = script[0].text.strip().split("window.mosaic.")
        line = [line.strip().strip(";") for line in lines if line_start in line][0]
        data = line[len(line_start) :].strip().strip("=")

        jobcards = json.loads(data)
        results = jobcards["metaData"]["mosaicProviderJobCardsModel"]["results"]
        jobs = [
            {
                "jobkey": result["jobkey"][:50],
                "url": f"/viewjob?jk={result['jobkey']}",
                "title": result["displayTitle"][:100],
                "company": result["company"][:100],
                "location": result["formattedLocation"][:100],
                "relative_time": result["formattedRelativeTime"][:50],
                # "attributes": result["taxonomyAttributes"],
            }
            for result in results
        ]
        return jobs
