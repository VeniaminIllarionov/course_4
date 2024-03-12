import pytest
from src.requests_hh import Request_HH
from src.class_vacansy import Vacansy


@pytest.fixture
def vacansy():
    vacs_list = Vacansy(300_000, 'Москва')
    return vacs_list


@pytest.fixture
def req():
    req_list = Request_HH('Разработчик')
    return req_list


def test_init(vacansy, req):
    assert req.name == 'Разработчик'
    req.save_info()
    assert vacansy.salary == 300000
    assert vacansy.city == 'Москва'
    vacansy.read_vacansy()
    assert vacansy.vacansy() == [{'id': '94550062', 'premium': False, 'name': 'TypeScript разработчик (Middle+/Senior)',
                                  'department': None, 'has_test': False, 'response_letter_required': False,
                                  'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                                  'salary': {'from': 300000, 'to': 450000, 'currency': 'RUR', 'gross': False},
                                  'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
                                  'sort_point_distance': None, 'published_at': '2024-03-11T17:47:03+0300',
                                  'created_at': '2024-03-11T17:47:03+0300', 'archived': False,
                                  'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94550062',
                                  'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/94550062?host=hh.ru',
                                  'alternate_url': 'https://hh.ru/vacancy/94550062', 'relations': [],
                                  'employer': {'id': '10457812', 'name': 'Савельев Георгий Анатольевич',
                                               'url': 'https://api.hh.ru/employers/10457812',
                                               'alternate_url': 'https://hh.ru/employer/10457812',
                                               'logo_urls': None,
                                               'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10457812',
                                               'accredited_it_employer': False, 'trusted': False},
                                  'snippet': {'requirement': 'Опыт Backend от 4 лет. Опыт TypeScript от 3 лет. '
                                                             'Приемлемый Frontend опыт в нашем стеке. '
                                                             'Отличное знание TypeScript, пишем...',
                                              'responsibility': 'Совместно с командой разрабатывать и сопровождать '
                                                                'проекты на всех этапах работы, от архитектуры до '
                                                                'оптимизации процессов. Создавать API для фронтенда...'}
                                     , 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
                                  'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
                                  'accept_temporary': False,
                                  'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                                  'accept_incomplete_resumes': False,
                                  'experience': {'id': 'moreThan6', 'name': 'Более 6 лет'},
                                  'employment': {'id': 'full', 'name': 'Полная занятость'},
                                  'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]

    assert vacansy.construction() == ['1.TypeScript разработчик (Middle+/Senior), \nЗарплата от: 300000, \n'
                                      'Зарплата до: 450000, \nТребование: Опыт Backend от 4 лет. '
                                      'Опыт TypeScript от 3 лет. Приемлемый Frontend опыт в нашем стеке. '
                                      'Отличное знание TypeScript, пишем..., \n'
                                      'Требуется: Совместно с командой разрабатывать и сопровождать проекты на всех '
                                      'этапах работы, от архитектуры до оптимизации процессов. '
                                      'Создавать API для фронтенда..., \nГород: Москва, '
                                      '\nСсылка на вакансию: https://hh.ru/vacancy/94550062']
    assert vacansy.top_vacansy() == 300000

