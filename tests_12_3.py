import runner as r
import runner_and_tournament as rt
import unittest


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner_1 = r.Runner('Саша')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner_2 = r.Runner('Даша')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_3 = r.Runner("Вова")
        runner_4 = r.Runner("Рома")
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.r1 = rt.Runner("Усейн", 10)
        self.r2 = rt.Runner("Андрей", 9)
        self.r3 = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1}, {elem}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        t1 = rt.Tournament(90, self.r1, self.r3)
        t1_result = t1.start()
        TournamentTest.all_results.append(t1_result)
        self.assertTrue(t1_result[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        t2 = rt.Tournament(90, self.r2, self.r3)
        t2_result = t2.start()
        TournamentTest.all_results.append(t2_result)
        self.assertTrue(t2_result[2], 'Ник')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        t3 = rt.Tournament(90, self.r1, self.r3, self.r3)
        t3_result = t3.start()
        TournamentTest.all_results.append(t3_result)
        self.assertTrue(t3_result[3], 'Ник')


if __name__ == "__main__":
    unittest.main()