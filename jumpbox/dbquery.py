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
"""This module handles database connectivity"""

import sys

from configuration import DBConnect


class DBHandler(object):

    # This function returns data from a query for all devices
    def all_devices_query(self):
        query_all_devices = '\
            SELECT dcim_device.name AS "Device Name", \
                   ipam_ipaddress.address AS "IP Address" \
            FROM dcim_device, ipam_ipaddress \
            WHERE dcim_device.primary_ip4_id = ipam_ipaddress.id \
            ORDER BY dcim_device.name ASC;'

        rows = self.DBConnect.fetcher(query_all_devices)
        return rows

    # This function returns data from a query for all sites
    def all_sites_query(self):
        query_all_sites = '\
            SELECT dcim_site.id, dcim_site.name, dcim_site.facility \
            FROM dcim_site \
            ORDER BY dcim_site.facility ASC;'

        rows = self.DBConnect.fetcher(query_all_sites)
        return rows

    # This function returns data from a query for devices from a single site
    def one_site_query(self, site_id):
        query_one_site = '\
            SELECT dcim_device.name AS "Device Name", \
                   ipam_ipaddress.address AS "IP Address" \
            FROM dcim_device \
                 JOIN ipam_ipaddress ON dcim_device.primary_ip4_id = \
                                        ipam_ipaddress.id \
            WHERE dcim_device.site_id = ' + str(site_id) + '\
            ORDER BY dcim_device.name ASC;'

        rows = self.DBConnect.fetcher(query_one_site)
        return rows
        