import pytest
from ..models import KeyModel, SharedEmail


class TestModels:
    @pytest.mark.django_db
    def test_model_keystorage(self):
        name = "postgresql"
        password = "password"
        keymodel = KeyModel.objects.create(name=name, password=password)
        assert keymodel.name == name
        assert keymodel.password == password

    @pytest.mark.django_db
    def test_model_sharedemail(self):
        email = "testtest.com"
        shared_email = SharedEmail.objects.create(email=email)
        assert shared_email.email == email
        assert shared_email.visited is False

