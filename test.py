import unittest
from solution import flatten

class Test(unittest.TestCase):
	def test_flatten_empty(self):
		self.assertEqual(flatten({}), {}, "wrong output")

	def test_flatten_unnested(self):
		d = {"a": 1,"b": 2,"c": 3}
		expected = {"a": 1, "b": 2, "c": 3}
		self.assertEqual(flatten(d), expected, "wrong output")

	def test_flatten_longnested(self):
		d = {"a": {"b": {"c": {"d": {"e": 1}}}}}
		expected = {"a.b.c.d.e": 1}
		self.assertEqual(flatten(d), expected, "wrong output")

	def test_flatten_longnested_and_unnestedattheend(self):
		d = {"a": {"b": {"c": {"d": {"e": 1, "f": 2, "g": 3}}}}}
		expected = {"a.b.c.d.e": 1, "a.b.c.d.f": 2, "a.b.c.d.g": 3}
		self.assertEqual(flatten(d), expected, "wrong output")

	def test_flatten_nested_and_unnested(self):
		d = {"a": {"b": {"c": 1}}, "d": 2}
		expected = {"a.b.c": 1, "d": 2}
		self.assertEqual(flatten(d), expected, "wrong output")
		
if __name__ == '__main__':
	unittest.main()