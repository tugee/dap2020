#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, param1):
        self.start = param1

    def write(self, param1):
        print(self.start + param1)
        # some statements


def main():
    pass

if __name__ == "__main__":
    main()
