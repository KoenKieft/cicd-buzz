from buzz import generator


def test_sample_single_word():
    L = ('foo', 'bar', 'foobar')
    word = generator.sample(L)
    assert word in L


def test_sample_multiple_words():
    L = ('foo', 'bar', 'foobar')
    words = generator.sample(L, 2)
    assert len(words) == 2
    assert words[0] in L
    assert words[1] in L
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
