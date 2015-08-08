# coding : utf8

__author__ = 'Kovaler'

import os
import sys
import shutil
import argparse

TEMPLATE_NAME = 'header.cpp'
default_folder = os.getcwd()
default_problem_set = "ABCDE"
default_contest_name = "CF Round #300"


def create_contest(name, problems, folder):
    """Creating directory with contest name, then creating folders for all problems in problem set
    and copying header to source files. Template header should be located in the same directory as script """
    contest_folder = os.sep.join([folder, name])
    os.mkdir(contest_folder)
    for problem in problems:
        problem_folder = os.sep.join([contest_folder, problem])
        print(problem_folder)
        os.mkdir(problem_folder)
        shutil.copy(os.sep.join([os.getcwd(), TEMPLATE_NAME]), problem_folder)
        os.rename(os.sep.join([problem_folder, TEMPLATE_NAME]), os.sep.join([problem_folder, problem])+'.cpp')


def create_path(path):
    """ Checking for chosen folder. If the path does not exists, then will create it """
    print(path)
    if not os.path.exists(path):
        os.makedirs(path)
    return


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default=default_contest_name)
    parser.add_argument('-p', '--problem_set', default=default_problem_set)
    parser.add_argument('-f', '--folder', default=default_folder)

    return parser


if __name__ == '__main__':
    arg_parser = create_parser()
    args = arg_parser.parse_args(sys.argv[1:])
    contest_name = args.name
    problem_set = args.problem_set
    active_folder = args.folder
    if len(problem_set) == 1:
        char = problem_set
        problem_set = [chr(i) for i in xrange(ord('A'), ord(char.upper()) + 1)]
    print problem_set
    create_path(active_folder)
    create_contest(contest_name, problem_set, active_folder)
