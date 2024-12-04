import pytest
import requests

class TestYD:
    def setup_method(self):
        self.headers = {
            'Authorization': 'token'
        }


    @pytest.mark.parametrize(
        'param, folder_name, status',
        (
                ('path', 'Image', 201),
                ('path', 'Image', 409),
                ('pat', 'Music', 400)

        )
    )
    def test_create_folder(self, param, folder_name, status):
        params = {
            param: folder_name
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params, headers=self.headers)
        assert response.status_code == status

    @pytest.mark.parametrize(
        'param, folder_name, status',
        (
                ('path', 'Image', 200),
                ('path', 'Music', 404),
                ('pat', 'Music', 400)

        )
    )
    def test_exists_folder(self, param, folder_name, status):
        params = {
            param: folder_name
        }
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params, headers=self.headers)
        assert response.status_code == status


    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'param, folder_name, status',
        (
                ('path', 'Im', 200),
                ('path', 'Music', 200),
                ('path', 'Video', 200)

        )
    )
    def test_not_exists_folder(self, param, folder_name, status):
        params = {
            param: folder_name
        }
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params, headers=self.headers)
        assert response.status_code == status

