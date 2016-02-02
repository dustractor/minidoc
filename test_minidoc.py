import unittest

import minidoc


class TestMinidoc(unittest.TestCase):

    def test_foo_is_foo(self):
        el_foo = str(minidoc.elem("foo"))
        an_foo = "<foo/>"
        self.assertEqual(el_foo,an_foo)

if __name__ == "__main__":
    unittest.main()
