from bs4 import BeautifulSoup


class IndeedJobParser:
    """Parser for Indeed job pages."""

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")
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

        # company_info = self.soup.select(
        #     "div[data-testid='jobsearch-CompanyInfoContainer']"
        # )
        # if company_info:
        #     job["company_info"] = str(company_info[0])

        # apply_button = self.soup.select("div#applyButtonLinkContainer button")
        # if apply_button:
        #     job["apply_url"] = apply_button[0].attrs["href"]

        # benefits = self.soup.select("div#benefits")
        # if benefits:
        #     job["benefits"] = str(benefits[0])

        description = self.soup.select("div#jobDescriptionText")
        if description:
            job["description"] = str(description[0])

        # salary_and_job_info = self.soup.select("div#salaryInfoAndJobType")
        # if salary_and_job_info:
        #     job["salary_and_job_info"] = str(salary_and_job_info[0])

        return job


class IndeedJobsListParser:
    """Parser for Indeed search results pages."""

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    def get_job_from_card(self, card):
        job = {
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

    def get_job_cards(self):
        self.jobs = []

        jobcards = self.soup.select("div#mosaic-provider-jobcards div.slider_container")
        for card in jobcards:
            try:
                job = self.get_job_from_card(card)
                self.jobs.append(job)
            except Exception as e:
                print(f"Error parsing job card: {e}\ncard={card}")

        return self.jobs

    def get_next_page_url(self):
        next_page = self.soup.select("link[rel='next']")
        if next_page:
            return next_page[0].attrs["href"]
        else:
            return None

    def get_previous_page_url(self):
        prev_page = self.soup.select("link[rel='prev']")
        if prev_page:
            return prev_page[0].attrs["href"]
        else:
            return None
