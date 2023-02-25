from hypothesis import given, strategies

from wordlist.word_list import WordList


@given(strategies.sets(strategies.text(), min_size=1), strategies.sets(strategies.text()))
def test_difference(first_set, second_set):
    first_word_list = WordList(first_set)
    second_word_list = WordList(second_set)

    unique_set = first_word_list.difference(second_word_list)
    if len(unique_set) == 0:
        assert all(i in second_set for i in first_set)
        return

    assert all(i in first_set for i in unique_set)
    assert not all(i in second_set for i in unique_set)


def test_difference_same_set():
    test_set = {'ab', 'bc'}
    first_list = WordList(test_set)
    second_list = WordList(test_set)
    unique_list = first_list.difference(second_list)
    assert 0 == len(unique_list)
