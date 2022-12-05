import allure
import requests
from jsonschema.validators import validate

from configuration.config import url
from jsonschemas.get_info import GetInfo


@allure.epic('Получение и создание списка людей')
class TestApp:

    @allure.title('Проверка сервиса на работоспособность {GET}')
    def test_get_health_check(self):
        response = requests.get(url + '/list')
        assert response.status_code == 200, 'Wrong status code'

    @allure.title('Получить список людей и их профессии')
    # @pytest.mark.parametrize(male, female)
    def test_get_people(self):
        response = requests.get(url + '/list')
        response_dict = response.json()
        jsonschema = GetInfo.get_info(self)
        validate(response_dict, jsonschema)

    @allure.title('Проверка сервиса на работоспособность {POST}')
    def test_post_health_check(self):
        body = {'name': 'Petr Petrov',
                'age': '25',
                'city': 'Moscow'}
        response = requests.post(url + '/add', json=body)
        assert response.status_code == 200, 'Wrong status code'

    @allure.title('Добавить новых людей в список')
    def test_add_people(self):
        body = {'name': 'Petr Petrov',
                'age': '25',
                'city': 'Moscow'}
        response = requests.post(url + '/add', json=body)
        response_dict = response.json()
        jsonschema = GetInfo.get_info(self)
        validate(response_dict, jsonschema)
