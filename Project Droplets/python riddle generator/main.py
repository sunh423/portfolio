from random import choice
from csv import writer
import string
import uuid


class MathRiddleGenerator:
    opr_allowed = {"add": "+", "subtract": "-", "multiply": "×", "divide": "÷"}

    def __init__(self, opr="add", pv1=2, pv2=2):
        self.opr = opr  # type of operator, by default, it's addition.
        # number of place values, for example, 2 digit number would be 2 (default). Only supports up to 3.
        self.pv1 = pv1
        self.pv2 = pv2
        self.alpha = string.ascii_uppercase
        self.pairs = {}
        self.unique = set()
        self.gen_pairs()
        self.write_pairs()

    def _pv_range(self, pv):
        if pv == 1:
            return range(1, 10)
        elif pv == 2:
            return range(10, 100)
        else:
            return range(100, 1000)

    def gen_pairs(self):
        for a in self.alpha:
            if self.opr == "add":
                b = choice(self._pv_range(self.pv1))
                c = choice(self._pv_range(self.pv2))
                d = b + c
                while d in self.unique:
                    b = choice(self._pv_range(self.pv1))
                    c = choice(self._pv_range(self.pv2))
                    d = b + c
                self.pairs.update({a: (b, c, d)})

    def write_pairs(self):
        while True:
            _unique = str(uuid.uuid4())[:6]
            try:
                with open(f"{_unique}_{self.opr}.csv", "x") as file:
                    break
            except FileExistsError:
                print(f"{_unique} file already exists!")

        with open(f"{_unique}_{self.opr}.csv", "w") as file:
            w = writer(file, delimiter=' ')
            for a in list(self.pairs.keys()):
                b, c, d = self.pairs[a]
                w.writerow(
                    [f'({a})', f'{b}', f'{MathRiddleGenerator.opr_allowed[self.opr]}', f'{c}', '=', f'{d}'])


MathRiddleGenerator()
