script="
from django.contrib.auth.models import User;

username = '$DJANGO_ADMIN_USER';
password = '$DJANGO_ADMIN_PASSWORD';
email = '$DJANGO_ADMIN_EMAIL';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Superuser created.');
else:
    print('Superuser creation skipped.');
"
printf "$script" | python manage.py shell