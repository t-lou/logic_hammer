import unittest

from logic_hammer import LogicHammer


class TestStringMethods(unittest.TestCase):
    @staticmethod
    def load_file(path: str):
        with open(path) as fi:
            content = fi.read()
        return content

    def test1(self):
        self.assertEqual(str(LogicHammer(self.load_file('tests/most_stupid'))),
                         '''hello world''')

    def test2(self):
        self.assertEqual(
            str(LogicHammer(self.load_file('tests/second_most_stupid'))),
            '''AND
  hello world
  world''')

    def test3(self):
        self.assertEqual(
            str(LogicHammer(self.load_file('tests/third_most_stupid'))), '''OR
  AND
    hello
    world
  c''')

    def test4(self):
        self.assertEqual(str(LogicHammer(self.load_file('tests/not_clever'))),
                         '''NOT
  clever''')

    def test5(self):
        self.assertEqual(
            str(LogicHammer(self.load_file('tests/all_stupid'))), '''AND
  NOT
    clever
  OR
    stupid
    silly silly silly
  confused plus
  hungry''')


if __name__ == '__main__':
    unittest.main()
