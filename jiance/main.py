import sys
sys.path.append('..')
from ftest import *
from action.SearchAction import SearchAction
from action.JianceAction import JianceAction
from action.AssetsAddAction import AssetsAddAction
from action.AssetsDelAction import AssetsDelAction


class Jiance():
    def __init__(self):
        self.testsuite = unittest.TestSuite()

    def testAll(self):
        self.testsuite.addTest(unittest.makeSuite(SearchAction))
        self.testsuite.addTest(unittest.makeSuite(JianceAction))
        self.testsuite.addTest(unittest.makeSuite(AssetsAddAction))
        self.testsuite.addTest(unittest.makeSuite(AssetsDelAction))
        return self.testsuite


if __name__ == "__main__":
    jiance = Jiance()
    TestRun(jiance.testAll())
    # unittest.TextTestRunner(verbosity=2).run(jiance.testAll())
