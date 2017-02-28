# Copyright (C) 2017 Bradley Sakdol <bsakdol@turnitin.com>
#
# This file is part of Jumpbox
#
# Jumpbox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from codecs import open

with open('jumpbox/_version.py') as version_file:
    exec (version_file.read())

setup(
    name='Jumpbox',
    version=__version__,
    zip_safe=False,
    description='Terminal based menu to manage SSH connections',
    packages=find_packages(exclude['docs']),
    include_package_data=True,
    install_requires=[
        'paramiko',
        'psycopg2',
    ], )
