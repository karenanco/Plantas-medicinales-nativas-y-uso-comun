"""
Management command to seed the database with 85 species of medicinal plants.

Usage:
    python manage.py load_plantas          # Load all species
    python manage.py load_plantas --force  # Reload even if data exists
"""

from django.core.management.base import BaseCommand, CommandError
from plantas.models import Planta
from plantas.data.plantas_data import PLANTAS_DATA


class Command(BaseCommand):
    help = "Seed the database with 85 species of medicinal plants from Chile."

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Force reload even if data already exists.",
        )

    def handle(self, *args, **options):
        # ── Check if data already exists ──────────────────────────────────────
        existing_count = Planta.objects.count()

        if existing_count > 0 and not options["force"]:
            self.stdout.write(
                self.style.WARNING(
                    f"⚠  La base de datos ya contiene {existing_count} plantas. "
                    "Usa --force para recargar."
                )
            )
            return

        if options["force"]:
            self.stdout.write(
                self.style.WARNING(f"🗑  Eliminando {existing_count} plantas existentes...")
            )
            Planta.objects.all().delete()

        # ── Load data ─────────────────────────────────────────────────────────
        created = 0
        for entry in PLANTAS_DATA:
            _, was_created = Planta.objects.get_or_create(
                nombre_cientifico=entry["nombre_cientifico"],
                defaults=entry,
            )
            if was_created:
                created += 1

        total = Planta.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f"✅  ¡Datos cargados exitosamente!\n"
            f"   • Nuevas plantas creadas: {created}\n"
            f"   • Total en base de datos: {total}"
        ))
