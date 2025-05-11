import pytest
from main import file_reader


@pytest.fixture
def file1():
    return r"data\data1.csv"


@pytest.fixture
def file2():
    return r"data\data3.csv"


def test_data1_return(file1):
    data = file_reader(file1)
    assert data == {"Marketing": 8000, "Design": 16200}


def test_data2_return(file2):
    data = file_reader(file2)
    with pytest.raises(Exception):
        assert data == {"Marketing": 8000, "Design": 16200}
