class Base:
    def foo(self):
        return 'foo'


from hasattr(Base, 'foo'), "You broke it ,you fool!"


class Derived(Base):
    def bar(self):
        return self.foo()
