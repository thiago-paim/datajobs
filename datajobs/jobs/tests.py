from unittest.mock import patch, call
from django.test import TestCase

from jobs.fixtures.indeed import pages, job_cards, job_details
from jobs.parsers import IndeedJobsListParser, IndeedJobParser
from jobs.scrapers import IndeedScraper


class IndeedJobsListParserTest(TestCase):
    def test_get_job_cards(self):
        parser = IndeedJobsListParser(pages["search-results-full"])
        cards = parser.get_job_cards()
        self.assertEqual(
            cards,
            job_cards["search-results-full"],
        )

    def test_get_next_page_url(self):
        parser = IndeedJobsListParser(pages["search-results-full"])
        next_page = parser.get_next_page_url()
        self.assertEqual(
            next_page, "/jobs?q=python+dados&l=Brasil&forceLocation=-1&start=10"
        )

    def test_get_empty_next_page_url(self):
        parser = IndeedJobsListParser(pages["search-results-short"])
        next_page = parser.get_next_page_url()
        self.assertEqual(next_page, None)

    def test_get_empty_previous_page_url(self):
        parser = IndeedJobsListParser(pages["search-results-full"])
        prev_page = parser.get_previous_page_url()
        self.assertEqual(prev_page, None)


class IndeedJobParserTest(TestCase):
    def test_get_job(self):
        parser = IndeedJobParser(pages["job-details-1"])
        job = parser.get_job()
        self.assertEqual(
            job,
            job_details["job-details-1"],
        )


class IndeedScraperTest(TestCase):
    @patch("jobs.scrapers.IndeedScraper.get_page")
    def test_search_jobs_by_url(self, get_page_mock):
        get_page_mock.side_effect = [
            pages["search-results-short"],
            pages["job-details-1"],
            pages["job-details-2"],
        ]
        scraper = IndeedScraper()
        jobs, next = scraper.search_jobs_by_url(url="/jobs?q=python+dados&l=Brasil")

        get_page_mock.assert_has_calls(
            [
                call("/jobs?q=python+dados&l=Brasil"),
                call("/viewjob?jk=ce75845b0f6a82e3"),
                call("/viewjob?jk=5d482db843f4b802"),
            ]
        )
        self.assertEqual(
            jobs,
            [
                job_details["job-details-1"],
                job_details["job-details-2"],
            ],
        )
        self.assertEqual(next, None)

    @patch("jobs.scrapers.IndeedScraper.search_jobs_by_url")
    def test_query_jobs(self, search_jobs_by_url_mock):
        search_jobs_by_url_mock.side_effect = [
            (
                [
                    job_details["job-details-1"],
                    job_details["job-details-2"],
                ],
                "/jobs?q=python+dados&l=Brasil&start=10",
            ),
            (
                [
                    job_details["job-details-1"],
                    job_details["job-details-2"],
                ],
                None,
            ),
        ]
        scraper = IndeedScraper()
        jobs = scraper.query_jobs(q="python+dados", l="Brasil")

        search_jobs_by_url_mock.assert_has_calls(
            [
                call("/jobs?q=python+dados&l=Brasil"),
                call("/jobs?q=python+dados&l=Brasil&start=10"),
            ]
        )
        self.assertEqual(
            jobs,
            [
                job_details["job-details-1"],
                job_details["job-details-2"],
                job_details["job-details-1"],
                job_details["job-details-2"],
            ],
        )
