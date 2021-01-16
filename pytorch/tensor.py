import unittest
from __future__ import print_function
import torch


class MyTestCase(unittest.TestCase):
    def test_create(self):
        # Construct a 5x3 matrix, uninitialized:
        x = torch.empty(5, 3)

        # Construct a randomly initialized matrix
        x = torch.rand(5, 3)
        print(x)

        # Construct a matrix filled zeros and of dtype long:
        x = torch.zeros(5, 3, dtype=torch.long)
        print(x)

        # Construct a tensor directly from data:
        x = torch.tensor([5.5, 3])
        print(x)

        x = x.new_ones(5, 3, dtype=torch.double)  # new_* methods take in sizes
        print(x)

        x = torch.randn_like(x, dtype=torch.float)  # override dtype!
        print(x)  # result has the same size

        # Get its size:
        print(x.size())

        self.assertEqual(True, True)

    def test_operations(self):
        # Addition: syntax 1
        x = torch.rand(5, 3)
        y = torch.rand(5, 3)
        print(x + y)

        # syntax 2
        print(torch.add(x, y))
        self.assertEqual(True, True)

        # Addition: providing an output tensor as argument
        result = torch.empty(5, 3)
        torch.add(x, y, out=result)
        print(result)

        # Addition: in-place, adds x to y.
        # Any operation that mutates a tensor in-place is post-fixed with an _.
        # For example: x.copy_(y), x.t_(), will change x.
        y.add_(x)
        print(y)

        # Resizing: If you want to resize/reshape tensor, you can use torch.view:
        x = torch.randn(4, 4)
        y = x.view(16)
        z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
        print(x.size(), y.size(), z.size())


if __name__ == '__main__':
    unittest.main()
