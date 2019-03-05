

name = ['Jack', 'Tom']


class B:

    def __init__(self, arg):
        self.b_ = []
        self.b_.append(arg)


class C:

    def __init__(self, arg):
        self.c_ = []
        for i in arg:
            self.c_.append(B(i))



if __name__ == '__main__':
    test = C(name)
    exit()
