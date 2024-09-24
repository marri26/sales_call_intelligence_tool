# Sales Call Intelligence Tool

## Installation Steps

Follow the steps below to set up the Sales Call Intelligence Tool on your local machine.

### 1. Create a Virtual Environment

First, create a virtual environment to manage your project's dependencies

```bash
python3 -m venv environment_name
```

### 2. Activate the Virtual Environment

Next, activate the virtual environment

```bash
source environment_name/bin/activate
```

### 3. Install Required Packages

Install the necessary packages listed in requirements.txt

```bash
pip3 install -r requirements.txt
```

### 4. Create a Django Superuser

To manage your Django application, create a superuser account

```bash
python3 manage.py createsuperuser
```

You will be prompted to enter a username, email address, and password.

### 5. Run the Development Server

Finally, start the Django development server

```bash
python3 manage.py runserver
```

You can access your application at http://127.0.0.1:8000/auditor.

