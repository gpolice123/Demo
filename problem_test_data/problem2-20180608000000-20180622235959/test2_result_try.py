# -*- coding: utf-8 -*-
"""
Code rally 2018 problem2
"""
import sys
import os
import threading,time,random


def solution(testline_num, user_num, user_testline):
    """

    """
    distribute_num = 0


    return distribute_num


def read_data(filename):
    testline_num, user_num, user_testline = 0, 0, []
    with open(filename) as rf:
        for line in rf:
            if line and line[0].isdigit():
                data = [int(d) for d in line.strip("\n\r").split(",")]
                if not testline_num:
                    testline_num, user_num = data[0:2]
                else:
                    user_testline.append(data)
    return testline_num, user_num, user_testline


def check_solution():
    if len(sys.argv) != 2:
        print "Usage: python %s data_file.csv" % sys.argv[0]
    elif not os.path.isfile(sys.argv[1]):
        print "File not exist or invalid %s" % sys.argv[1]
    else:
        testline_num, user_num, user_testline = read_data(sys.argv[1])
        print solution(testline_num, user_num, user_testline)


if __name__ == '__main__':
    user_testline = []
    solution(20, 10, user_testline)
