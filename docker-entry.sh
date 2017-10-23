 django server
# ATM using the dev built-in server .. will move later to nginx maybe

 pew in ffa-cdr-admin python manage.py migrate

# Running createsuperuser should be done manually by the admin upon docker-compose up for example
# pew in FFA_ES_SPLITTER python manage.py createsuperuser --no-input --username admin

# launch syslog
syslogd

# run server
pew in ffa-cdr-admin  python manage.py runserver 0.0.0.0:8009 | logger -t "runserver" &

# wait 1 second for the cron above to send its start output to syslog
sleep 1

# tail the logs
tail -f /var/log/messages

