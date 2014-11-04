# encoding=utf8
# author:shellvon

import argparse
import opt_config

parser = argparse.ArgumentParser(
    description='The %(prog)s by shellvon',
    epilog="""
                爬虫->22mm.cc上->美女图片
            """
    )
arguments = opt_config.optional_arguments
map(lambda x: parser.add_argument(x, **arguments[x]), arguments)
test = parser.parse_args()
print test.n, test.o, test.l,
