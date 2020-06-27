#test_activebuffer.py



import unittest

from render import Action, ActiveBuffer


def test_func(s=None):
    print(s)
    return s


def test_store(writer, vals):
    for val in vals:
        print(f'Writing {val}')
        writer(val)



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
        self.assertEqual(s, nb.actions['test_func']())

    
    def test_multiprocess_put(self):
        nb = ActiveBuffer()
        vals = [0, 1, 2]
        nb.bind(test_store, writer=nb.write, vals=vals)

        nb.run('test_store')
        read = [nb.read() for _ in range(len(vals) + 1)]
        self.assertEqual(len(read), len(vals) + 1)
        self.assertIsNone(read[-1])


    def test_rewrite_buffer(self):
        nb = ActiveBuffer()
        vals = [0, 1, 2]
        nb.bind(test_store, writer=nb.write)
        nb.run('test_store', vals=vals)

        nb.teardown()
        self.assertIsNone(nb.read())

        vals = [100, 200, 300]
        nb.bind(test_store, writer=nb.write)  # Must rebind writer here because its set up that way for testing.
        nb.run('test_store', vals=vals)
        read = [nb.read() for _ in range(len(vals) + 1)]
        self.assertEqual(len(read), len(vals) + 1)
        self.assertIsNone(read[-1])
