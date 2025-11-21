**MySite**

A small Django demo project with example apps: `blog`, `api` (custom user), `accounts`, and `memebers`.

**Project Summary**

- **Purpose**: Demo/evaluation project showing a Django site with a custom `User` model in the `api` app, REST framework settings, and a management command to populate sample data.
- **Django version used**: 5.2.7 (see `mysite/settings.py` header).

**Requirements**

- Python 3.11+ (Django 5.x requires modern Python; use the version that matches your environment).
- pip or Pipenv for dependency management. There's a `Pipfile` in the repository.

**Quick Setup (Windows PowerShell)**

1. Create and activate a virtual environment

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

2. Install dependencies (example)

```
pip install django==5.2.7 djangorestframework djangorestframework-simplejwt django-cors-headers
```

Or, using Pipenv:

```
pipenv install --dev
pipenv shell
```

Note: this project does not include a `requirements.txt` by default; create one with `pip freeze > requirements.txt` after installing packages.

**Database & Migrations**

1. Create migrations and apply them:

```
python manage.py makemigrations
python manage.py migrate
```

2. Common migration error and how to fix it:

- Error: `InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency api.0001_initial` means the DB record shows `admin` applied but `api` (dependency) not applied. Options:
  - If you can delete development DB: remove `db.sqlite3` and re-run `makemigrations` and `migrate`.
    ```powershell
    Remove-Item db.sqlite3
    python manage.py makemigrations
    python manage.py migrate
    ```
  - Unapply `admin`, apply `api`, then reapply remaining migrations:
    ```powershell
    python manage.py migrate admin zero
    python manage.py makemigrations api
    python manage.py migrate api
    python manage.py migrate
    ```
  - If the `api` tables already exist but migrations are not recorded, fake the migration (use with caution):
    ```powershell
    python manage.py makemigrations api
    python manage.py migrate api --fake 0001_initial
    python manage.py migrate
    ```

Always back up `db.sqlite3` before running unapply/--fake commands.

**Populate the database (sample data)**

- This project contains a management command defined in `api/management/commands/populate_db.py`.
- Run it by command name (do NOT append `.py`):

```
python manage.py populate_db
```

- If Django reports `Unknown command: 'populate_db'`:
  - Ensure the `api` app is in `INSTALLED_APPS` in `mysite/settings.py` (it is by default).
  - Ensure `__init__.py` exists in both `api/management/` and `api/management/commands/`.
    ```powershell
    New-Item -ItemType File -Path .\api\management\__init__.py -Force
    New-Item -ItemType File -Path .\api\management\commands\__init__.py -Force
    ```

**Run server and common commands**

```
python manage.py runserver
python manage.py createsuperuser
python manage.py test
```

**Pip / Network troubleshooting**

- If `pip install` fails with network/DNS errors (`getaddrinfo failed` or `Failed to establish a new connection`):
  - Check DNS and connectivity:
    ```powershell
    nslookup pypi.org
    Test-NetConnection pypi.org -Port 443
    ```
  - Make sure you are not behind an unconfigured proxy. Set proxy env vars in PowerShell for the session:
    ```powershell
    $env:HTTP_PROXY='http://proxyhost:port'
    $env:HTTPS_PROXY='http://proxyhost:port'
    python -m pip install djangorestframework --index-url https://pypi.org/simple --trusted-host pypi.org --trusted-host files.pythonhosted.org
    ```
  - If you cannot access PyPI at all, download `.whl` files on a machine with internet and install them locally:
    ```powershell
    python -m pip install C:\path\to\djangorestframework-*.whl
    ```

**Project layout (top-level)**

- `manage.py` - Django management script
- `mysite/` - project settings (`mysite/settings.py`, `urls.py`, etc.)
- `api/` - custom user model and API code (`models.py`, `management/commands/populate_db.py`, migrations)
- `blog/`, `memebers/`, `accounts/` - example apps
- `db.sqlite3` - SQLite database (development)

**Notes & Next steps**

- If you want I can:
  - Create a `requirements.txt` from the current environment.
  - Add a short CONTRIBUTING section or Docker dev instructions.
  - Run through migrations locally and validate the `populate_db` command (I can guide you through running the commands below).

---

Commands summary (copyable):

```
# activate env (PowerShell)
.\.venv\Scripts\Activate.ps1

# migrations
python manage.py makemigrations
python manage.py migrate

# populate data
python manage.py populate_db

# run dev server
python manage.py runserver
```
