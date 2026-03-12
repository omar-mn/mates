set -o errexit

pip install -t req.txt

python manage.py collectstatics --no-input

python manage.py migrate
