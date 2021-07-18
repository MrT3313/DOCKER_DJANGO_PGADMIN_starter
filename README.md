# Welcome

> This is a docker based Django Rest API w/ Django Rest Framework & pgAdmin

# Usage

1. Run Database Containers
  - postgres container : `pg_container`
  - pgAdmin container : `pgadmin4_container`
  > from dev/
  ```cli
  make docker-dev
  ```

2. DB Setup: Migrations & Superuser

   > depending on the state of your docker volumes you might have to:
   >
   > - re-create & re-run the database migrations
   > - create new superuser

    - Enter Django Container Terminal
        - `make djTerminal`
    - Make Migrations
        > from Django Terminal
        - `python manage.py makemigrations`
    - Run Migrations
        > from Django Terminal
        - `python manage.py migrate`
    - Create Super User
        > from Django Terminal
        - `python manage.py createsuperuser`

    - Exit terminal
        -`exit`

3. Login to pgAdmin
    - navigate to: `localhost:5050`
    - login:
        - username: `admin@admin.com`
        - password: `admin`

4. Create & Configure Server within pgAdmin

    > 🚨 debug creating this in the docker-compose environment _JSON_PATH environment argument

    - right click "Servers" > "Create" > "Server..."
        - General > name: `local_django_postgres`
        - Connection > Host
            - `db`
        - Connection > Port
            - `5432`
        - Connection > Username
            - `postgres`
        - Connection > Password
            - `postgres`

5. Explore Django Admin
    - ADMIN PANEL: `localhost:8000/admin`
    - Login w/ superuser creds (or any previously created user)