import inspect
from pprint import pprint
from types import ModuleType
from typing import Dict, Union, Any, List


def introspection_info(obj):
    result: dict[str, Union[Union[str, list[str], ModuleType, None], Any]] = {
        'type': type(obj),
        'attribute': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': inspect.getmodule(obj),
        'module_name': introspection_info.__module__,}
    return result


class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.info()

    def info(self):
        print(f'My name {self.name}, I am a {self.school} student')


number_info1 = introspection_info(42)
pprint(number_info1)
