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

* Start the containers, and the API will run on http://localhost:8000/

    ```bash
    docker compose up -d
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


* To monitor running tasks check Celery Flower: http://localhost:8888/

* In case you want to stop all the tasks, you can purge the tasks queue:

    ```bash
    docker exec -it datajobs-celery-1 celery -A datajobs purge
    ```


### Testing

* Enter Django shell inside the container

    ```bash
    docker exec -it datajobs-django-1 bash
    python3 manage.py shell
    ```

* Then: 

    ```python
    from jobs.scrapers import IndeedScraper
    scraper = IndeedScraper(q="python+dados", headless=False)
    jobs = scraper.run()
    ```



#### Errors found

* `URLError: <urlopen error [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1131)>`
    * Seems to be a temporary error; retrying after a while works