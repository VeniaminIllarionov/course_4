import pytest
from src.class_vacansy import Vacansy
from src.requests_hh import Request_HH


@pytest.fixture
def vac():
    vacs_list = Vacansy(240_000, 'Москва')
    return vacs_list


@pytest.fixture
def req():
    re_list = Request_HH('Разработчик')
    return re_list


def test_init1(req):
    assert req.name == 'Разработчик'
    req.get_url()
    req.status_api()
    req.save_info()


def test_init2(vac):
    assert vac.salary == 240000
    assert vac.city == 'Москва'
    assert vac.vacansy() == [{'id': '94660310', 'premium': False, 'name': 'React разработчик (middle+)',
                              'department': None, 'has_test': False, 'response_letter_required': False,
                              'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                              'salary': {'from': 250000, 'to': None, 'currency': 'RUR', 'gross': False},
                              'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва',
                                                                                      'street': 'бульвар Энтузиастов',
                                                                                      'building': '2',
                                                                                      'lat': 55.746481,
                                                                                      'lng': 37.682619,
                                                                                      'description': None,
                                                                                      'raw': 'Москва, бульвар '
                                                                                             'Энтузиастов, 2',
                                                                                      'metro': None,
                                                                                      'metro_stations': [],
                                                                                      'id': '15331850'},
                              'response_url': None, 'sort_point_distance': None,
                              'published_at': '2024-03-13T09:50:29+0300',
                              'created_at': '2024-03-13T09:50:29+0300', 'archived': False,
                              'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94660310',
                              'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/94660310?host=hh.ru',
                              'alternate_url': 'https://hh.ru/vacancy/94660310', 'relations': [],
                              'employer': {'id': '10755944', 'name': 'Дингилевская Маргарита Васильевна',
                                           'url': 'https://api.hh.ru/employers/10755944',
                                           'alternate_url': 'https://hh.ru/employer/10755944',
                                           'logo_urls': None,
                                           'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10755944',
                                           'accredited_it_employer': False, 'trusted': False},
                              'snippet': {'requirement': 'Коммерческий опыт разработки SPA (React + Redux). '
                                                         'Высокий уровень знания JavaScript/TypeScript. '
                                                         'Отличные знания HTML, CSS (Sass). GIT. ',
                                          'responsibility': 'Разработкой клиентской части веб и'
                                                            ' мобильного приложения (PWA) на основе предоставленных '
                                                            'дизайн-макетов и спецификаций. Оптимизацией интерфейсов. '
                                                            'Разработкой и/или...'}, 'contacts': None,
                              'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
                              'working_time_intervals': [], 'working_time_modes': [],
                              'accept_temporary': False,
                              'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                              'accept_incomplete_resumes': False, 'experience': {'id': 'between3And6',
                                                                                 'name': 'От 3 до 6 лет'},
                              'employment': {'id': 'full', 'name': 'Полная занятость'},
                              'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]
    assert vac.construction() == ['1.React разработчик (middle+), \nЗарплата от: 250000, \nЗарплата до: 0, '
                                  '\nТребование: Коммерческий опыт разработки SPA (React + Redux). '
                                  'Высокий уровень знания JavaScript/TypeScript. Отличные знания HTML, CSS (Sass). GIT.'
                                  ' , \nТребуется: Разработкой клиентской части веб и мобильного приложения (PWA) '
                                  'на основе предоставленных дизайн-макетов и спецификаций. Оптимизацией интерфейсов. '
                                  'Разработкой и/или..., \nГород: Москва, '
                                  '\nСсылка на вакансию: https://hh.ru/vacancy/94660310']
    assert vac.top_vacansy() == 250000
