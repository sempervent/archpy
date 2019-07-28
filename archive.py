#!/usr/bin/env python3
import os
import sys
import pathlib
import patoolib
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[0m'
    UNDERLINE = '\033[4m'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', action='store',
            dest='root_dir', help='The directory to parse \
                    and zip all subdirectories', default='',
                    type=str)
    parser.add_argument('-o', '--output-directory', action='store',
            dest='output_dir', help='Where should the zipped files be stored')
    parser.add_argument('-z', '--zip-format', action='store', default='zip',
            dest='zip_format', help='The format to use for archiving')
    parser.add_argument('-v', '--verbosity', action='count', \
            help='Make the program talk more', dest='verbose', default=0)
    parser.add_argument('-c', '--checksum', action='store_true',
            dest='checksum', help='Should a checksum file be generated')
    parser.add_argument('-t', '--test', action='store_true', \
            default='store_false', dest='test')
    parser.set_defaults(root_dir = os.path.dirname(os.path.realpath(__file__)),
            output_dir = os.path.dirname(os.path.realpath(__file__)),
                verbosity=0, test=False)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if args.verbose > 0:
        if args.test:
            print( bcolors.OKBLUE + ' ===> ' + 'running as ' + \
                    bcolors.WARNING + 'test' + bcolors.ENDC)
    if args.verbose > 2:
        print( bcolors.OKBLUE + ' ===> ' + bcolors.OKGREEN + \
                ' retrieving direcotries within: ' + \
                bcolors.ENDC  + ''.join(args.root_dir))
    dirs = os.listdir(args.root_dir)
    if args.verbose > 2:
        print(bcolors.OKBLUE + ' ===> ' + bcolors.OKGREEN + \
                'Directories found:\n\t' + bcolors.ENDC + \
                '\n\t'.join(dirs))
    for d in dirs:
        if args.verbose > 0:
            print(bcolors.OKBLUE + ' ====> ' + bcolors.ENDC + \
                    'creating file %s' % d)
        archive_out = os.path.join(args.output_dir, d) + '.' + args.zip_format
        if args.verbose > 1:
            print(bcolors.OKBLUE + ' ====>  ' + bcolors.ENDC + \
                    '  Creating archive %s' % archive_out)
        outpath = os.path.join(args.root_dir, d)
        if not args.test:
            if args.verbose > 0:
                print(bcolors.OKGREEN + ' ====> ' + bcolors.ENDC +  archive_out)
                print(bcolors.OKGREEN + ' ====> ' + bcolors.ENDC + outpath)
            patoolib.create_archive("%s" % archive_out, \
                    (outpath + '/'))
            


