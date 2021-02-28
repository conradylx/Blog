# BlogWebsite

This is a simple application that demonstrates what I learned about creating blogs.

## Prerequisites

You must have the following installed if you want launch project from your IDE:
- Python 3
- Django

## Running in development

### Database

It is possible to run the app with no database content, but there will be no posts or comments to show.

To run with a database, you will need to add some products manually or type in the terminal:

- py manage.py makemigrations
- py manage.py migrate

### Running the application
Prepare the app:

```bash
pip install -r requirements.txt
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Screenshots will be uploaded soon!
