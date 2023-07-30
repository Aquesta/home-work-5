from wallet import refill, check_balance, purchase, write_history
from victory import peoples, sample_from_dict, check_answer, get_names


def test_refill():
    # пополнение баланса на 200 рублей при текущем 100
    assert refill(200, 100) == 300
    assert refill(100, 100) == 200
    assert refill(300, 200) == 500


def test_check_balance():
    # проверка на отрицательный баланс
    assert check_balance(100, 200)
    assert check_balance(200, 300)
    assert check_balance(100, 50) == False


def test_purchase():
    assert purchase(100, 200) == 100
    assert purchase(200, 400) == 200
    assert purchase(200, 100) == 100


def test_write_history():
    history = {}
    write_history('cola', 100, history)
    assert history == {'cola': 100}


def test_sample_from_dict():
    assert len(sample_from_dict(peoples, 5)) == 5
    assert len(sample_from_dict(peoples, 3)) == 3


def test_check_answer():
    assert check_answer(peoples, '07.10.1952', 'Путин')


def test_get_names():
    assert get_names(peoples) == ['Пушкин', 'Ленин', 'Сталин', 'Ельцин', 'Путин']