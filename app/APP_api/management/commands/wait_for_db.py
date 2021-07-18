"""
Django command to wait for the db to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    '''DJango command to wait for database to be available'''

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                # TODO: research self.check() more
                self.check()
                print('GOOD TO GO', self.check())
                db_up = True
            except (Psycopg2OpError, OperationalError):
                print('not ready :(', self.check())
                self.stdout.write('Database unavailable, waiting 1 second ')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is ready!'))