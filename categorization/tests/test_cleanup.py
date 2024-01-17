import pytest

from pkg.cleanup import clean_data, remove_punctuation, remove_stopwords, remove_states


@pytest.mark.parametrize('punctuation_string, expected_reulst',[
    ('This function, removes all the! punctuation marks$?', 'This function removes all the punctuation marks')
])
def test_remove_punctuation(punctuation_string, expected_reulst):
    assert remove_punctuation(punctuation_string) == expected_reulst


@pytest.mark.parametrize('stopword_string, expected_reulst',[
    ('a', ''),
    ('r.e.m.o.v.e', 'r.e.m.o.v.e')
])
def test_remove_stopwords(stopword_string, expected_reulst):
    assert remove_stopwords(stopword_string) == expected_reulst


@pytest.mark.parametrize('text, expected_result',[
    ('China', 'China'),
    ('New York', '')
])
def test_remove_states(text, expected_result):
    assert remove_states(text) == expected_result


if __name__ == "__main__":
    test_remove_states('NC', '')