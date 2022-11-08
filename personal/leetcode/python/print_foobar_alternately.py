import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.f = threading.Event()
        self.b = threading.Event()

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.f.set()
            self.b.wait()
            self.b.clear()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            self.f.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.b.set()
            self.f.clear()


if __name__ == "__main__":
    f = FooBar(100)

    def printFoo():
        print("foo", flush=True, end="")

    def printBar():
        print("bar", flush=True, end="")

    t1 = threading.Thread(target=f.foo, args=(printFoo,))
    t2 = threading.Thread(target=f.bar, args=(printBar,))
    t1.start()
    t2.start()
