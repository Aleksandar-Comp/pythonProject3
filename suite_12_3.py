import unittest
import tests_12_3 as t

rt_tt = unittest.TestSuite()
rt_tt.addTest((unittest.TestLoader().loadTestsFromTestCase(t.RunnerTest)))
rt_tt.addTest((unittest.TestLoader().loadTestsFromTestCase(t.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rt_tt)
