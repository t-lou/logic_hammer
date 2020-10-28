import unittest

from logic_hammer import LogicHammer


class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(str(LogicHammer('tests/most_stupid')),
                         '''hello world''')

    def test2(self):
        self.assertEqual(str(LogicHammer('tests/second_most_stupid')), '''AND
  hello world
  world''')

    def test3(self):
        self.assertEqual(str(LogicHammer('tests/third_most_stupid')), '''OR
  AND
    hello
    world
  c''')

    def test4(self):
        self.assertEqual(str(LogicHammer('tests/not_clever')), '''NOT
  clever''')

    def test5(self):
        self.assertEqual(
            str(LogicHammer('tests/all_stupid')), '''AND
  NOT
    clever
  OR
    stupid
    silly silly silly
  confused plus
  hungry''')


if __name__ == '__main__':
    unittest.main()
