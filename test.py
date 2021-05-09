import unittest
from crossword import Crossword, Variable
from generate import CrosswordCreator


class TestGenerate(unittest.TestCase):
    def setUp(self):
        structure = "data/structure0.txt"
        words = "data/words0.txt"
        self.crossword = Crossword(structure, words)

    def test_revise(self):
        creator = CrosswordCreator(self.crossword)
        creator.enforce_node_consistency()
        var_x = Variable(4, 1, "across", 4)
        var_y = Variable(0, 1, "down", 5)
        old_domain_x = creator.domains.get(var_x)
        old_domain_y = creator.domains.get(var_y)
        self.assertTrue(creator.revise(var_x, var_y))
        new_domain_x = creator.domains.get(var_x)
        new_domain_y = creator.domains.get(var_y)
        self.assertTrue(old_domain_y == new_domain_y)
        self.assertTrue(len(old_domain_x) > len(new_domain_x))

    def test_assignment_is_complete(self):
        creator = CrosswordCreator(self.crossword)
        creator.enforce_node_consistency()



if __name__ == '__main__':
    unittest.main()
