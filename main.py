# -*- coding: utf-8 -*-

import os
import sys
import time


def mkdir(target):
    target = (target.strip()).rstrip('\\')
    if not os.path.exists(target):
        return os.makedirs(target)
    else:
        return False


def output(target, content):
    with open(target, 'a') as f:
        f.write(content + '\n')
    f.close


def hi(content):
    return content


def main():
    now = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(time.time()))
    content = '{} {}'.format(now, sys.argv[1])
    runtime = './runtime/'

    mkdir(runtime)
    output(runtime + 'tester.log', content)


if __name__ == '__main__':
    main()

# vim: noai:ts=4:sw=4
