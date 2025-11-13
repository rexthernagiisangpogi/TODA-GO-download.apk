# Django Download Site

A beautiful, responsive download site built with Django for distributing your application.

## Features

- Modern, responsive design using Tailwind CSS
- Clean download page with app information
- System requirements display
- Installation instructions
- File download functionality
- Admin interface for content management

## Setup Instructions

### 1. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 4. Add Your App Files

1. Place your application installer in the `media/app/` directory
2. Update the `download_url` in `downloader/views.py` to point to your file
3. Customize the app information in `downloader/views.py`

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your download site.

## Customization

### App Information

Edit `downloader/views.py` to customize:
- App name and version
- Description and features
- System requirements
- Download file path

### Styling

The template uses Tailwind CSS. You can customize:
- Colors by changing the CSS classes in `downloader/templates/downloader/home.html`
- Layout and components
- Icons (using Font Awesome)

### Static Files

For custom CSS/JS files:
1. Create a `static/` directory in the project root
2. Add your files to `static/css/` or `static/js/`
3. Load them in the template using `{% load static %}`

## File Structure

```
windsurf-project/
├── download_site/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── downloader/             # Main app
│   ├── templates/
│   │   └── downloader/
│   │       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/                  # File downloads
│   └── app/
│       └── .gitkeep
├── manage.py
├── requirements.txt
└── README.md
```

## Production Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Set up a proper database (PostgreSQL recommended)
4. Configure static file serving
5. Use a web server like Nginx + Gunicorn

## License

This project is open source and available under the MIT License.
# TODA-GO-download.apk
