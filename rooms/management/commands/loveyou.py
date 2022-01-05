from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    def add_arguments(selfm, parser):
        parser.add_argument(
            "--times",
            help="How many time do you want me to tell you thet give me money",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
