import runner
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    def test_walk(self):
        rn = runner.Runner(name='Бегунъ')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn = runner.Runner(name='Бегунъ')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):
        rna = runner.Runner(name='RNA')
        rnb = runner.Runner(name='RnB')
        for _ in range(10):
            rna.run()
            rnb.walk()
        self.assertNotEqual(rna.distance, rnb.distance)

if __name__ == '__main__':
    unittest.main()
