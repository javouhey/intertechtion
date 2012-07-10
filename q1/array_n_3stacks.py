#!/usr/bin/env python
# Copyright 2012 Gavin Bong.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

from operator import itemgetter

# labels to identify which stack to use
S1, S2, S3 = range(3)

class Facade(object):
    """
    Exposes an API for 3 stacks that are 
    internally stored in a single list.
    """
    RECOGNIZED_LABELS = [S1, S2, S3]

    def __init__(self):
        self.store = []

    def push(self, value, stack=S1):
        '''Pushes a value on the supplied stack. Defaults to S1.

        .. raises ValueError if ``value`` is None.
        '''
        if value is None:
            raise ValueError("None not accepted as value")

        if stack in self.RECOGNIZED_LABELS:
            self.store.append((stack, value))

    def pop(self, stack=S1):
        '''Pops a value from the supplied stack. Defaults to S1.

        .. raises ValueError if stack is empty.
        '''
        filtered = [x for x in self.store if itemgetter(0)(x) == stack]
        if filtered:
            found = filtered.pop()
            self.store.remove(found)
            return found[1]
        else:
            raise ValueError('Nothing in stack')

def main():
    threestack = Facade()
    threestack.push('aa')
    threestack.push('bb', S2)
    threestack.push('bc', S2)
    
    assert threestack.pop(S2) == 'bc'
    assert threestack.pop(S2) == 'bb'
    assert threestack.pop() == 'aa'

    try:
        threestack.pop(stack=S3)
        assert 1 == 2 # should not come here
    except ValueError:
        assert 1 == 1

if __name__ == '__main__':
    main()