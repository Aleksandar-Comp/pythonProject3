class Introspection_info:
    def __init__(self, name):
        self.name = name
        self.type = self.get_type()
        self.attributes = self.get_attributes()
        self.methods = self.get_methods()
        self.module = self.get_module()


    def get_type(self):
        return type(self.name)

    def get_attributes(self):
        return dir(self.name)

    def get_methods(self):
        methods = [meth for meth in self.attributes if callable(getattr(self.name, meth))]
        return methods

    def get_module(self):
        return self.name.__class__.__module__

    def __str__(self):
        return (f'name : {self.name} \ntype: {self.type}\nattributes : {self.attributes} \n'
                f'methods: {self.methods} \nmodule : {self.module}')


number_info = Introspection_info(42)
print(number_info)