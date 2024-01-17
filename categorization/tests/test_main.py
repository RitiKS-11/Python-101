import pytest

from pkg.main import ngrams, get_notes

@pytest.fixture
def filepath():
    return 'test-data.csv'

def test_get_notes(filepath):
    expected_reuslt= ['Travel and Tourism Site for Vermont ', 'See historical snapshot at: http://web.archive.org/web/20080120044716/http://www.1800arkansas.com/  ', '2-1-1 VIRGINIA is a service of the Virginia Department of Social Services provided in partnership with the Council of Community Services, the Family Resource and Referral Center, The Planning Council, the United Way of Central Virginia, and the United Way of Greater Richmond and Petersburg. ']
    assert expected_reuslt == get_notes(filepath)


@pytest.mark.parametrize('sentence, ngram, expected_result', [
    ('Hello Everyone', 1, ['Hello', 'Everyone']),
    ('Not every principle herein has to be strictly followed',
     2,
     ['Not every', 'every principle', 'principle herein', 'herein has', 'has to', 'to be', 'be strictly', 'strictly followed'])
])

def test_ngrams(sentence, ngram, expected_result):
    assert ngrams(sentence, ngram) == expected_result



if __name__ == "__main__":
    # test_ngrams(
        # 'Not every principle herein has to be strictly followed', 
        # 2,
        # ['Not every', 'every principle', 'principle herein', 'herein has', 'has to', 'to be', 'be strictly', 'strictly followed'])

    test_get_notes('test-data.csv')