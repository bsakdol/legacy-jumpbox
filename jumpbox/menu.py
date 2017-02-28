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
"""This module handles the menu system"""

from database import DBHandler
from formatter import FormatMenu


class Menu(object):
    def __init__(self):
        MENU = "menu"
        COMMAND = "command"
        PROMPT = "prompt"

        menu_all_devices = FormatMenu().format_devices(
            DBHandler().all_devices_query())

        menu_all_sites = FormatMenu().format_sites(
            DBHandler().all_sites_query())

        self.main_menu = {
            'title':
            "Main Menu",
            'subtitle':
            "Please select an option...",
            'type':
            MENU,
            'options': [
                {
                    'title': "All Devices",
                    'subtitle': "Please select a device...",
                    'type': MENU,
                    'options': menu_all_devices
                },
                {
                    'title': "Devices by Site",
                    'subtitle': "Please select a site...",
                    'type': MENU,
                    'options': menu_all_sites
                },
            ]
        }
