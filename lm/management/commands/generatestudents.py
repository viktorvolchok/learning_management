from django.core.management import BaseCommand

from faker import Faker

from lm.models import Subject, Student

fake = Faker(locale="uk")


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()

            Student.objects.create(first_name=first_name, last_name=last_name)

        for subject in Subject.objects.all():
            subject.students.add(
                Student.objects.order_by('?').first()
            )
