import unittest
import os.path as osp

from mipack.utils import module_path


class TestPath(unittest.TestCase):

    def test01_module_path(self):
        self.assertEqual(osp.basename(module_path()), 'mipack')
