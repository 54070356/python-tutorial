import argparse
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        parser = argparse.ArgumentParser(description="Run MTC Task.")

        # Data Parameters
        parser.add_argument("--arg1",
                            nargs="?",
                            default="arg1 value",
                            help="this is arg1")
        args, unknown = parser.parse_known_args()


        args.arg2 = 'arg2 value'
        print(args.arg2)

        argparse.Namespace(a="b")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
