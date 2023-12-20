from abc import ABC, abstractmethod
from typing import Any

from core.context import WindowContext


class Component(ABC):
    """
    The core stateless component class that is used to render an element tree.
    """
    @abstractmethod
    def render(self, cx: WindowContext) -> Any:
        pass


class Render(ABC):
    """
    Interface that is used to render the different components on screen.
    """

    @staticmethod
    @abstractmethod
    def new(cx: WindowContext):
        pass

    @abstractmethod
    def render(self, cx: WindowContext) -> Component:
        pass
