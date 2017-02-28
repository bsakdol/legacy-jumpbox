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
"""This module handles formatting of data"""

import re

from database import DBHandler


class FormatMenu(object):

    # This function formats the data from device specific queries to menu syntax
    def format_devices(self, query_data):

        # Remove any CIDR notation
        x = 0
        while x < len(query_data):
            if query_data[x][1].find('/') >= 0:
                ip_addr, sep, mask = query_data[x][1].partition('/')
                query_data[x] = (query_data[x][0], ip_addr)
            x += 1

        # Remove device member number from hostname
        x = 0
        while x < len(query_data):
            if re.search('-\d$', query_data[x][0]):
                hostname = re.sub('-\d$', '', query_data[x][0])
                query_data[x] = (hostname, query_data[x][1])
            x += 1

        # Conver the raw data to the syntax used by the menu
        x = 0
        device_list = list()
        device_dict = dict()
        while x < len(query_data):
            device_dict['ip_addr'] = query_data[x][1]
            device_dict['title'] = query_data[x][0]
            device_dict['type'] = "command"
            device_list.append(device_dict.copy())
            x += 1

        return device_list

    # This function formats the data from site specific queries to menu syntax
    def format_sites(self, query_data):
        x = 0
        site_list = list()
        site_dict = dict()
        while x < len(query_data):
            site_dict['site_id'] = query_data[x][0]
            site_dict['title'] = query_data[x][1]
            site_dict['subtitle'] = query_data[x][2]
            site_dict['type'] = "menu"

            site_dict['options'] = self.format_devices(
                DBHandler().one_site_query(site_dict['site_id']))

            site_list.append(site_dict.copy())
            x += 1

        return site_list
