import abc
from abc import ABCMeta, abstractclassmethod

class Entity(object, metaclass=abc.ABCMeta):
    @classmethod
    @abstractclassmethod
    def event(self, event):
        raise NotImplementedError("Event not implemented")

    @classmethod
    @abstractclassmethod
    def update(self, elapsed_time):
        raise NotImplementedError("Update not implemented")

    @classmethod
    @abstractclassmethod
    def draw(self, window):
        raise NotImplementedError("Draw not implemented")