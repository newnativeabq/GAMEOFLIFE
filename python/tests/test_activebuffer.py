#test_activebuffer.py



import unittest

from render import Action, ActiveBuffer


def test_func(s=None):
    print(s)
    return s


class TestActiveBuffer(unittest.TestCase):
    

    def test_action(self):
        s = 'test'
        a = Action(test_func, s=s)
        self.assertEqual(s, a())


    def test_activebuffer_create(self):
        newActiveBuffer = ActiveBuffer()


    def test_bind(self):
        nb = ActiveBuffer()
        s = 'test'
        nb.bind(test_func, s=s)

        

    