from dicts import DefaultDict


def get_bigrams(words):
	"""
	Given an array of words, returns a dictionary of dictionaries,
	containing occurrence counts of bigrams.
	"""
	d = DefaultDict(DefaultDict(0))
	for (w1, w2) in zip([None] + words, words + [None]):
		d[w1][w2] += 1
	return d


def convert_file_to_bigrams(filename):
	"""
	Takes a file as input and returns a bigram dictionary.
	"""
	return get_bigrams(open(filename).read().split())
