#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: badpasta <beforget@gmail.com> 
#
# Environment:
# Python power by version 2.7
#
# Create at: 2017-05-16 15:37:57
# Request: [MySql, request, argparse]

import sys
import os
import setuptools
from version import __VERSION__


def _setup():
    setuptools.setup(
        name='stafftools',
        version=__VERSION__,
        description='It is a simple script what be used to sync user data from stip & rt to staff.',
        author='Jingyu Wang',
        author_email='jingyu15@staff.sina.com.cn',
        url='',
        install_requires=['requests', 'mysql-connector-python-rf', 'argparse', 'PyYaml'],
        packages=setuptools.find_packages("src"),
        package_dir={'': 'src'},
        include_package_data = True,
        entry_points={
            'console_scripts': [
                #'stafftools-api=stafftools.tools.api:start_api_server',
                'stafftools-useradd=stafftools.tools.api:user_info_add',
                'stafftools-userleft=stafftools.tools.api:user_check_left',
                'stafftools-extenduser=stafftools.tools.api:import_extend_user',
                ]
            },
        classifiers=[
            'Development Status :: 4 - Beta Development Status',
            'Environment :: Console',
            'Topic :: Utilities',
        ],
    )

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'publish':
            os.system('make publish')
            sys.exit()
        elif sys.argv[1] == 'release':
            if len(sys.argv) < 3:
                type_ = 'patch'
            else:
                type_ = sys.argv[2]
            assert type_ in ('major', 'minor', 'patch')

            os.system('bumpversion --current-version {} {}'
                      .format(__VERSION__, type_))
            sys.exit()

    _setup()


if __name__ == '__main__':
    main()


