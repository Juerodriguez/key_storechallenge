import pytest
from django.test import Client


@pytest.fixture
def create_password_dict():
    return {'name': 'postgresql', 'password': 'lavidadiaria1'}


class TestKeyViews:
    @pytest.mark.django_db
    def test_view_get_keystorage(self):
        client = Client()
        response = client.get("/key_storage/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_view_post_created_keystorage(self, create_password_dict):
        client = Client()
        response = client.post("/key_storage/",
                               data=create_password_dict,
                               content_type="application/json")

        assert response.data["name"] == "postgresql"
        assert response.status_code == 201


class TestKeyDetailView:
    @pytest.mark.skip
    def test_view_detail_get_keystorage(self):
        client = Client()
        response = client.get("/key_storage/")
        assert response.status_code == 200

    @pytest.mark.skip
    def test_view_detail_update_keystorage(self, create_password_dict):
        client = Client()
        response = client.post("/key_storage/",
                               data=create_password_dict,
                               content_type="application/json")

        assert response.data["name"] == "postgresql"
        assert response.status_code == 201
