import pytest
from src.json_work import Json_Work
from src.class_vacansy import Vacansy
from src.requests_hh import Request_HH


@pytest.fixture
def vacansy():
    vacs_list = Vacansy(300_000, 'Москва')
    return vacs_list


@pytest.fixture
def req():
    re_list = Request_HH('Разработчик')
    return re_list


def test_init1(req):
    assert req.name == 'Разработчик'
    req.save_info()


def test_init2(vacansy):
    assert vacansy.salary == 300000
    assert vacansy.city == 'Москва'
    assert vacansy.vacansy() == [{'id': '94344863', 'premium': False, 'name': 'Разработчик SAP ABAP (Senior)',
                                  'department': None, 'has_test': False, 'response_letter_required': False,
                                  'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                                  'salary': {'from': 330000, 'to': 380000, 'currency': 'RUR', 'gross': False},
                                  'type': {'id': 'open', 'name': 'Открытая'}, 'address': None,
                                  'response_url': None, 'sort_point_distance': None,
                                  'published_at': '2024-03-06T15:03:11+0300',
                                  'created_at': '2024-03-06T15:03:11+0300',
                                  'archived': False,
                                  'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94344863',
                                  'show_logo_in_search': None, 'insider_interview': None,
                                  'url': 'https://api.hh.ru/vacancies/94344863?host=hh.ru',
                                  'alternate_url': 'https://hh.ru/vacancy/94344863',
                                  'relations': [], 'employer': {'id': '4968559', 'name': 'IT-OTS',
                                                                'url': 'https://api.hh.ru/employers/4968559',
                                                                'alternate_url': 'https://hh.ru/employer/4968559',
                                                                'logo_urls':
                                                                    {'original': 'https://img.hhcdn.ru/employer-logo-'
                                                                                 'original/799742.png',
                                                                     '90': 'https://img.hhcdn.ru/employer-logo'
                                                                           '/3639855.png',
                                                                     '240': 'https://img.hhcdn.ru/employer-logo'
                                                                            '/3639856.png'},
                                                                'vacancies_url': 'https://api.hh.ru/vacancies'
                                                                                 '?employer_id=4968559',
                                                                'accredited_it_employer': False, 'trusted': True},
                                  'snippet': {'requirement': 'Опыт программирования на языках высокого уровня '
                                                             'от 5 лет. - Опыт работы с высоконагруженными '
                                                             'системами. - Участие в проектах внедрения SAP ERP...',
                                              'responsibility': 'Выполнять задачи по разработке программных решений в '
                                                                'SAP системах на основании технических заданий, '
                                                                'полученных от функциональных консультантов и в '
                                                                'соответствии...'}, 'contacts': None,
                                  'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
                                  'working_time_intervals': [], 'working_time_modes': [],
                                  'accept_temporary': False,
                                  'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                                  'accept_incomplete_resumes': False,
                                  'experience': {'id': 'moreThan6', 'name': 'Более 6 лет'},
                                  'employment': {'id': 'full', 'name': 'Полная занятость'},
                                  'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]
    assert vacansy.construction() == ['1.Разработчик SAP ABAP (Senior), \nЗарплата от: 330000, \nЗарплата до: 380000, '
                                      '\nТребование: Опыт программирования на языках высокого уровня от 5 лет. - Опыт '
                                      'работы с высоконагруженными системами. - Участие в проектах внедрения SAP '
                                      'ERP..., \nТребуется: Выполнять задачи по разработке программных решений в SAP '
                                      'системах на основании технических заданий, полученных от функциональных '
                                      'консультантов и в соответствии..., \nГород: Москва, \nСсылка на вакансию: '
                                      'https://hh.ru/vacancy/94344863']
    assert vacansy.top_vacansy() == 330000
