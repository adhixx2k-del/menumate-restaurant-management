#!/usr/bin/env bash
# build.sh - Render build script for MenuMate
# This runs every time Render deploys your app

set -o errexit  # Exit on any error

# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Collect static files (WhiteNoise serves these)
python manage.py collectstatic --no-input

# 3. Run database migrations (creates/updates tables in Supabase)
python manage.py migrate

# 4. Create superuser (admin) if one doesn't exist yet
#    Uses env vars: DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_EMAIL
python manage.py create_superuser_if_not_exists
