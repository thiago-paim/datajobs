# datajobs


## How to setup


* Create a local `.env` file by creating a copy of the sample file:

    ```bash
    cd datajobs
    cp .env.sample .env
    ```

* Ensure you have [Docker](https://docs.docker.com/engine/) up and running, and then build the containers: 

    ```bash
    docker compose build
    ```


## How to run

* Start the containers, and the app will run on http://localhost:8000/

    ```bash
    docker compose up -d
    ```

* To scrape a query from Indeed:

    ```bash
    docker exec -it datajobs-django-1 python3 manage.py scrape_indeed_query "python+dados" "Remoto"
    ```

* To stop your app:

    ```bash
    docker compose down
    ```


### Monitoring

* In case you want a closer look on the database objects, you can use Django's builtin Admin app.

    * Create a super user:

        ```bash
        docker exec -it datajobs-django-1 python3 manage.py createsuperuser
        ```
        
    * Then use it to login into the admin: http://localhost:8000/admin/


### Testing

* Run automated tests:

    ```bash
    docker exec -it datajobs-django-1 python3 manage.py test
    ```

* Enter Django shell inside the container

    ```bash
    docker exec -it datajobs-django-1 bash
    python3 manage.py shell
    ```

* Then: 

    ```python
    from jobs.tasks import scrape_indeed_list_url
    url = "/jobs?q=python+dados&l="
    created, updated = scrape_indeed_list_url(url)
    ```

    ```python
    from jobs.scrapers import IndeedScraper
    scraper = IndeedScraper()
    params = {"q": "python+django", "l": "Remoto"}
    url = scraper.get_query_url(params)
    parser = scraper.get_parsed_search_page(url=url)
    ```


#### Errors found

* `URLError: <urlopen error [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1131)>`
    * Seems to be a temporary error; retrying after a while works