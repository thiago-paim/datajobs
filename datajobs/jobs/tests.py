from bs4 import BeautifulSoup
import datetime
import pytz
from unittest.mock import patch, call
from django.test import TestCase

from jobs.fixtures.indeed import pages, job_cards
from jobs.parsers import IndeedJobsListParser


class IndeedJobsListParserTest(TestCase):
    def test_get_job_cards(self):
        parser = IndeedJobsListParser(pages["q-python-dados"])
        cards = parser.get_job_cards()
        self.assertEqual(
            cards,
            job_cards["q-python-dados"],
        )

    def test_get_next_page_url(self):
        parser = IndeedJobsListParser(pages["q-python-dados"])
        next_page = parser.get_next_page_url()
        self.assertEqual(next_page, "/jobs?q=python+dados&l=Brasil&start=10")

    def test_get_previous_page_url(self):
        parser = IndeedJobsListParser(pages["q-python-dados"])
        prev_page = parser.get_previous_page_url()
        self.assertEqual(prev_page, None)
