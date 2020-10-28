kOpBinary = set(['AND', 'OR'])
kOpUnary = set(['NOT'])
kBegin = '('
kEnd = ')'
kSep = ' '


class Node(object):
    class _Parser(object):
        def __init__(self, content: str):
            self.content = content

        def __iter__(self):
            return self

        def __next__(self):
            if bool(self.content):
                if self.content[0] == kBegin:
                    id_end = -1
                    level = 0
                    for i, c in enumerate(self.content):
                        if c == kBegin:
                            level += 1
                        if c == kEnd:
                            level -= 1
                        if level == 0:
                            id_end = i
                            break
                    assert id_end > 0, 'unbalanced quote in {}'.format(
                        self.content)
                    this = self.content[1:id_end]
                    self.content = self.content[(id_end + 1):]
                else:
                    id_end = self.content.find(kSep)
                    id_end = id_end if id_end >= 0 else len(self.content)
                    this = self.content[:id_end]
                    self.content = self.content[(id_end + 1):]
                while bool(self.content) and self.content[0] == kSep:
                    self.content = self.content[1:]
                return this
            else:
                raise StopIteration

    def __init__(self, data: str, depth: int = 0):
        self._tab = ' ' * 2 * depth
        self._depth = depth

        elems = list(self._Parser(data))
        assert len(elems) >= 1, 'data not read from "{}"'.format(data)
        while len(elems) == 1 and self.has_element_operator(elems[0]):
            elems = list(self._Parser(elems[0]))
        self._operator = None
        if elems[0] in kOpUnary:
            assert len(
                elems
            ) == 2, 'unary operator can only have one element: {}'.format(
                elems)
            self._operator = elems[0]
            self._elements = [Node(elems[1], depth + 1)]
        elif len(elems) > 1 and elems[1] in kOpBinary:
            assert len(
                elems
            ) % 2 == 1, 'number of elements should be uneven: {}'.format(elems)
            assert len(set(
                elems[1::2])) == 1, 'mixed operations: {}'.format(elems)
            self._operator = elems[1]
            self._elements = [Node(elem, depth + 1) for elem in elems[::2]]
        else:
            self._element = kSep.join(elems)

    def __str__(self):
        if self._operator is None:
            return ' ' * 2 * self._depth + self._element
        else:
            return ' ' * 2 * self._depth + self._operator + '\n' + '\n'.join(
                [str(node) for node in self._elements])

    @staticmethod
    def has_element_operator(data: str):
        return any(' {} '.format(op) in data
                   for op in kOpBinary) or any('{} '.format(op) in data
                                               for op in kOpUnary)


class LogicHammer(object):
    def __init__(self, content: str):
        self._parsed = self.parse(content)

    @staticmethod
    def parse(data: str):
        assert bool(data)
        return Node(data)

    def __str__(self):
        return str(self._parsed)
