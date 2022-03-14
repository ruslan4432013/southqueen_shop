import requests
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from faker import Faker
import random

fake = Faker('ru')


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num_products', type=int, nargs='?', default=15)

    def handle(self, *args, **options):
        num_products = options.get('num_products')

        models = [Product, ProductCategory]

        for model in models:
            model.objects.all().delete()

        category_list = []

        for _ in range(5):
            name = fake.language_name()
            description = fake.text(max_nb_chars=160)
            category = ProductCategory.objects.create(name=name, description=description)
            category_list.append(category)


        url = 'https://loremflickr.com/480/480'
        list_with_content = []
        for i in range(num_products):
            response = requests.get(url)
            with open(f'media/products_images/img_{i}.jpg', 'wb+') as f:
                f.write(response.content)
                list_with_content.append(f'products_images/img_{i}.jpg')

        for _ in range(num_products):
            data = {'category': random.choice(category_list),
                    'name': fake.text(max_nb_chars=20),
                    'image': random.choice(list_with_content),
                    'short_desc': fake.text(max_nb_chars=60),
                    'description': fake.text(max_nb_chars=200),
                    'price': fake.pyint(),
                    'quantity': fake.pyint()}

            Product.objects.create(**data)