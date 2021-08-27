from django.test import TestCase
import random
import string


from products.models import Product
from users.models import CustomUser


class ProductTest(TestCase):

    def test_product_creation(self):
        random_name = self._random_product_values(),
        random_phone = random.randint(1111, 99999)
        random_user = CustomUser.objects.create_user(phone=str(random_phone))
        product = Product.objects.create(
            name=random_name,
            owner=random_user
        )
        print(f"Name {product.name} | Owner {product.owner.phone}")

    def _random_product_values(self):
        some_name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
        return some_name
