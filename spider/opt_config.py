# coding=utf8
# author:shellvon

import argparse
import os


class ReadableDir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values[0]
        message = "readable_dir:{0} is not a readable dir".format(prospective_dir)
        try:
            if not os.path.exists(prospective_dir):
                os.mkdir(prospective_dir)
        except:
            raise argparse.ArgumentTypeError(message)
        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError(message)
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace, self.dest, prospective_dir)
        else:
            raise argparse.ArgumentTypeError(message)

OPTIONAL_ARGUMENTS = {
    '-n':
        {
            'help': 'the number of the thread(default is 10)',
            'dest': 'thread_num',
            'type': int,
            'default': 10
        },
    '-o':
        {
            'help': 'the output dirs of the picture store(default is ./pics)',
            'action': ReadableDir,
            'dest': 'output',
            'nargs': 1,
            'default': './pics'
        },
    '-l':
        {
            'help': 'the limits of the picture when program exit(default no limits).',
            'dest': 'limit',
            'type': int,
            'default': 0
        },
    '-t':
        {
            'help': 'delay to display the progress info for a given number of seconds (default 10 seconds).',
            'dest': 'timeout',
            'type': float,
            'default': 10
        },
    '-v':
        {
            'help': 'show versions',
            'action': 'version',
            'version': '%(prog)s 0.0.1 by shellvon'
        }
}

PARSER = argparse.ArgumentParser(
    description='The %(prog)s by shellvon',
    epilog="""
            爬虫->22mm.cc上->美女图片
    """
)


def get_opt(arguments=OPTIONAL_ARGUMENTS, parser=PARSER):
    map(lambda x: parser.add_argument(x, **arguments[x]), arguments)
    return parser.parse_args()
if __name__ == '__main__':
    pass
