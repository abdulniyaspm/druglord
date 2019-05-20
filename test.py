import unittest


loader = unittest.TestLoader()
suite = loader.discover('test/')
runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(suite)
