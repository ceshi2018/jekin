import pytest
import allure

class Test_02:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title='第十')
    def test_01(self):
        print('pass')
        allure.attach('test1','这是第一个')
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title='第十一')
    def test_02(self):
        allure.attach('test2', '这是第二个')
        print('fail')
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title='第十二')
    def test_03(self):
        allure.attach('test3', '这是第三个')
        print('fail')
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title='第十三')
    def test_04(self):
        allure.attach('test4', '这是第四个')
        print('fail')
        assert False

