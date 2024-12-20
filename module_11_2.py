from pprint import pprint


def introspection_info(obj):
    type_ = type(obj).__name__
    attr = [x for x in dir(obj) if not callable(getattr(obj, x))]
    methods = [y for y in dir(obj) if callable(getattr(obj, y))]
    module = type(obj).__module__
    dict_intro = {
        'type': type_,
        'attributes': attr,
        'methods': methods,
        'module': module
    }
    return dict_intro


number_info = introspection_info(42)
pprint(number_info, sort_dicts=False)


class Agro():
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(f'Это растение называется {self.name}')


a = Agro('Лопух')
a_info = introspection_info(a)
pprint(a_info, sort_dicts=False)
