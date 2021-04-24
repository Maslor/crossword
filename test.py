import unittest
from crossword import Crossword, Variable
from generate import CrosswordCreator


class TestGenerate(unittest.TestCase):
    def setUp(self):
        structure = "data/structure0.txt"
        words = "data/words0.txt"
        self.crossword = Crossword(structure, words)

    def test_get_overlap_indexes_x_across(self):
        creator = CrosswordCreator(self.crossword)
        var_x = Variable(4, 1, "across", 4)
        var_y = Variable(0, 1, "down", 5)
        overlap_indexes = creator.get_overlap_indexes(var_x, var_y)
        print(overlap_indexes)
        self.assertTrue((0, 4) == overlap_indexes)

    def test_get_overlap_indexes_x_down(self):
        creator = CrosswordCreator(self.crossword)
        var_x = Variable(0, 1, "down", 5)
        var_y = Variable(4, 1, "across", 4)
        overlap_indexes = creator.get_overlap_indexes(var_x, var_y)
        print(overlap_indexes)
        self.assertTrue((4, 0) == overlap_indexes)

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


if __name__ == '__main__':
    unittest.main()
