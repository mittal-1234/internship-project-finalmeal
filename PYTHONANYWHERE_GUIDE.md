# PythonAnywhere Deployment Guide for FinalMeal

Follow these steps to get your project live on [mittaljangada.pythonanywhere.com](https://mittaljangada.pythonanywhere.com/).

## 1. Upload Your Code
The easiest way is to use Git. Open a **Bash Console** on PythonAnywhere and run:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```
*(Replace the URL with your actual GitHub repository URL)*

## 2. Set Up Virtual Environment
In the same Bash console, create a virtual environment and install dependencies:
```bash
mkvirtualenv --python=/usr/bin/python3.10 finalmeal-env
pip install -r requirements.txt
```
*Note: If you are using a different Python version, adjust the command accordingly.*

## 3. Configure the Web Tab
Go to the **Web** tab on PythonAnywhere and click **"Add a new web app"**.
1.  Select **Manual Configuration** (do NOT select "Django").
2.  Choose the Python version you used in step 2 (e.g., 3.10).

### Path Settings:
-   **Source code:** `/home/mittaljangada/YOUR_REPO_NAME`
-   **Working directory:** `/home/mittaljangada/YOUR_REPO_NAME`
-   **Virtualenv:** `/home/mittaljangada/.virtualenvs/finalmeal-env`

## 4. Configure WSGI File
In the **Web** tab, look for the "WSGI configuration file" link. Click it and replace the entire content with this:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/mittaljangada/YOUR_REPO_NAME'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'meal_buddy.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
*(Make sure to replace `YOUR_REPO_NAME` with the actual folder name where your code is)*

## 5. Static Files Mapping
In the **Web** tab, scroll down to the **Static files** section and add these entries:

| URL | Path |
| :--- | :--- |
| `/static/` | `/home/mittaljangada/YOUR_REPO_NAME/staticfiles/` |

Then, go back to your **Bash Console** and run:
```bash
python manage.py collectstatic
```

## 6. Run Migrations
In the **Bash Console**, set up your database:
```bash
python manage.py migrate
```

## 7. Reload
Go back to the **Web** tab and click the big green **Reload** button. Your site should now be live!
