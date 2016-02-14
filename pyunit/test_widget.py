import unittest

class WidgetTestCase(unittest.TestCase):
	def setUp(self):
		self.widget = Widget('The widget')

	def tearDown(self):
		self.widget.dispose()
		self.widget = None

	def test_default_size(self):
		self.assertEqual(self.widget.size(), (50, 50),
			"incorrect default size")

	def test_resize(self):
		self.widget.resize(100, 150)
		self.assertEqual(self.widget.size(), (100, 150),
			"wrong size after resize")

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
	unittest.TextTestRunner(verbosity=2).run(suite)
