import data
def test_positive_assert_code_200(): #тест на проверку 200 статуса
    current_code = data.response_get_an_order_by_number
    assert current_code.status_code == 200