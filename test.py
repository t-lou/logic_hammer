import unittest

from logic_hammer import LogicHammer


class TestHammered(unittest.TestCase):
    @staticmethod
    def load_file(path: str):
        with open(path) as fi:
            content = fi.read().strip()
        return content

    def test1(self):
        path = 'tests/most_stupid'
        expectation = '''hello world'''
        self.assertEqual(str(LogicHammer(self.load_file(path))), expectation)

    def test2(self):
        path = 'tests/second_most_stupid'
        expectation = '''AND
  hello world
  world'''
        self.assertEqual(str(LogicHammer(self.load_file(path))), expectation)

    def test3(self):
        path = 'tests/third_most_stupid'
        expectation = '''OR
  AND
    hello
    world
  c'''
        self.assertEqual(str(LogicHammer(self.load_file(path))), expectation)

    def test4(self):
        path = 'tests/not_clever'
        expectation = '''NOT
  clever'''
        self.assertEqual(str(LogicHammer(self.load_file(path))), expectation)

    def test5(self):
        path = 'tests/all_stupid'
        expectation = '''AND
  NOT
    clever
  OR
    stupid
    silly silly silly
  confused plus
  hungry'''
        self.assertEqual(str(LogicHammer(self.load_file(path))), expectation)


if __name__ == '__main__':
    unittest.main()
