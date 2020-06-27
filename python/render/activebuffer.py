"""
Active Buffer

    Bind functions, arguments, and keep alive tasks/endpoints to Buffer
"""

from .buffer import Buffer

from multiprocessing import Process


class Action():
    def __init__(self, func, **kwargs):
        self.func = func 
        self.kwargs = kwargs
    
    def __call__(self):
        return self.func(**self.kwargs)




class ActiveBuffer(Buffer):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actions = {}

    def bind(self, func, **kwargs):
        self.actions.update(
            {func.__name__:Action(func=func, **kwargs)}
            )

    def start(self):
        pass