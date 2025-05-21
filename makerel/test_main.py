import unittest
from transformpath import TransformPath

class TestMain(unittest.TestCase):
    def test_example(self):
        # Example test case
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    class TestTransformPath(unittest.TestCase):

        def test_update_line(self):
            tp = TransformPath("/foo/bar/")
            line = "make[1]: Entering directory '/foo/bar/makerel/subdir'"
            lineout = tp.transform_line(line)
            self.assertEqual(lineout, line)

            line = "./file.c:123: error: ..."
            lineout = tp.transform_line(line)
            self.assertEqual(lineout, "makerel/subdir/file.c:123: error: ...")
           

    if __name__ == '__main__':
        unittest.main()