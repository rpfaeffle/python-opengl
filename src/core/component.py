class Component(object):
    """
    Interface that is used to render the different components on screen.
    """

    def __init__(self):
        self.children: list[Component] = []

    def add_child(self, child):
        self.children.append(child)

    def render(self, context):
        for child in self.children:
            child.render(context)
