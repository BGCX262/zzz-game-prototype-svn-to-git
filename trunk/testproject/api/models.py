import unittest
from testproject.api.tests import userstests


def suite():
    return unittest.TestLoader().loadTestsFromModule(userstests, False)