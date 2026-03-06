import pytest

@pytest.mark.xfail(reason="Найден баг в приложении, из-за которого тест падает")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Баг уже исправлен, но тест все еще висит с маркировкой xfail")
def test_without_bug():
    ...

