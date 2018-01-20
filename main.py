# -*- coding: utf-8 -*-


def output(target, content):
    with open(target, 'a') as f:
        f.write(content + '\n')
    f.close


def hi(content):
    return content


def main():
    pass


if __name__ == '__main__':
    main()

# vim: noai:ts=4:sw=4
