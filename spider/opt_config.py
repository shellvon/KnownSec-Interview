# encoding=utf8
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

optional_arguments = {
    '-n':
        {
            'help': 'the number of the thread(default is 10)',
            'type': int,
            'nargs': 1,
            'default': 10
        },
    '-o':
        {
            'help': 'the output dirs of the picture store(default is ./pics)',
            'action': ReadableDir,
            'nargs': 1,
            'default': './pics'
        },
    '-l':
        {
            'help': 'the limits of the picture when program exit(default no limits).',
            'type': int,
            'nargs': 1,
            'default': 0
        },
    '-v':
        {
            'help': 'show versions',
            'action': 'version',
            'version': '0.0.1'
        }
}

if __name__ == '__main__':
    pass
