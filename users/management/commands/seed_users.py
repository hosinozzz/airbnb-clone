from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(selfm, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many users do yo want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} ユーザー　作成　成功！"))
