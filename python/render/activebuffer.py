"""
Active Buffer

    Bind functions, arguments, and keep alive tasks/endpoints to Buffer
"""

from .buffer import Buffer

from functools import partial
from multiprocessing import Process


class Action():
    def __init__(self, func, **kwargs):
        self.func = partial(func, **kwargs)
    
    def __call__(self, **kwargs):
        return self.func(**kwargs)




class ActiveBuffer(Buffer):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {}

    def bind(self, func, **kwargs):
        self.actions.update(
            {func.__name__:Action(func=func, **kwargs)}
            )

    def run(self, name, **kwargs):
        p = Process(target=self.actions[name], kwargs=kwargs)
        p.start()
        p.join()