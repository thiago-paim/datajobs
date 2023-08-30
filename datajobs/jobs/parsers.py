from bs4 import BeautifulSoup


class IndeedJobParser:
    """
    Parser para páginas de detalhes de vagas da Indeed.
    Exemplo de página: https://br.indeed.com/viewjob?jk=80f70cdd34aa97e8',
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")
        self.job = self.get_job()

    def get_job(self):
        job = {
            "html": None,
            "canonical_url": None,
            "title": None,
            "company_info": None,
            "apply_href": None,
            "benefits": None,
            "description": None,
        }

        job["html"] = str(self.soup)
        job["canonical_url"] = self.soup.select("link[rel='canonical']")[0].attrs[
            "href"
        ]
        job["title"] = self.soup.select("h1 span")[0].string
        job["company_info"] = self.soup.select(
            "div[data-testid='jobsearch-CompanyInfoContainer']"
        )
        apply_button = self.soup.select("div#applyButtonLinkContainer button")
        if apply_button:
            job["apply_href"] = apply_button[0].attrs["href"]

        benefits = self.soup.select("div#benefits")
        if benefits:
            job["benefits"] = benefits[0]

        description = self.soup.select("div#jobDescriptionText")
        if description:
            job["description"] = description[0]

        return job


class IndeedJobsListParser:
    """
    Parser para páginas de listagem de vagas da Indeed.
    Exemplo de página: https://br.indeed.com/jobs?q=python+dados&l=Brasil&vjk=80f70cdd34aa97e8
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    def get_job_from_card(self, card):
        job = {
            "title": None,
            "a": None,
            "data-jk": None,
            "href": None,
            "company_name": None,
            "company_location": None,
            "metadata": None,
            "job_snippet": None,
            "posted_date": None,
        }
        job["title"] = card.select("h2.jobTitle span")[0].string
        job["a"] = card.select("a")[0]
        job["data-jk"] = card.select("a")[0].attrs[
            "data-jk"
        ]  # Parece ser o ID do anúncio
        job["href"] = card.select("a")[0].attrs["href"]

        company_name = card.select("span.companyName")
        if company_name:
            job["company_name"] = company_name[0]

        company_location = card.select("div.companyLocation")
        if company_location:
            job["company_location"] = company_location[0]

        metadata = card.select("div.metadata")
        if metadata:
            job["metadata"] = metadata[0]

        job_snippet = card.select("div.job-snippet")
        if job_snippet:
            job["job_snippet"] = job_snippet[0]

        job["posted_date"] = card.select("table.jobCardShelfContainer span.date")[0]

        return job

    def get_job_cards(self):
        self.jobs = []

        jobcards = self.soup.select("div#mosaic-provider-jobcards div.slider_container")
        for card in jobcards:
            job = self.get_job_from_card(card)
            self.jobs.append(job)

        return self.jobs
