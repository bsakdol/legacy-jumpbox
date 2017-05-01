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
"""This module handles the Jumpbox UI"""

import curses
import curses.panel
import os

from menu import Menu
from _version import __version__


class JumpboxUI(object):
    def __init__(self, stdscr):
        self.stdscr = stdscr

        curses.start_color()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(1)

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.highlight = curses.color_pair(1)
        self.normal = curses.A_NORMAL

        self.processmenu(Menu().main_menu)

    def processmenu(self, menu, parent=None):
        optioncount = len(menu['options'])
        exitmenu = False

        while not exitmenu:
            selected = self.runmenu(menu, parent)

            if selected == optioncount:
                exitmenu = True

            elif menu['options'][selected]['type'] == "menu":
                self.stdscr.clear()
                self.processmenu(menu['options'][selected], menu)
                self.stdscr.clear()

            elif menu['options'][selected]['type'] == "command":
                curses.def_prog_mode()
                os.system('reset')
                username = raw_input('Username: ')
                os.system('ssh ' + username + '@' + menu['options'][selected][
                    'ip_addr'])
                self.stdscr.clear()
                curses.reset_prog_mode()
                curses.curs_set(1)
                curses.curs_set(0)

            elif menu['options'][selected]['type'] == "prompt":
                curses.def_prog_mode()
                os.system('reset')
                ip_address = raw_input('IP / Hostname: ')
                os.system('clear')
                username = raw_input('Username: ')
                os.system('ssh ' + username + '@' + ip_address)
                self.stdscr.clear()
                curses.reset_prog_mode()
                curses.curs_set(1)
                curses.curs_set(0)

    def runmenu(self, menu, parent):
        self.stdscr.refresh()

        if parent is None:
            lastoption = 'Exit'
        else:
            lastoption = 'Return to the %s menu' % parent['title']

        optioncount = len(menu['options'])
        pos = 0
        oldpos = None
        scroller = 0
        cmd = None

        termy, termx = self.stdscr.getmaxyx()
        viewport = termy - 8
        height, width = optioncount + 3, termx - 4
        top, left = 5, 3

        pad = curses.newpad(height, width)

        while cmd != ord('\n'):
            if pos != oldpos:
                oldpos = pos
                self.stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
                self.stdscr.addstr(1, 2, 'NetOps Jumpbox', curses.A_UNDERLINE)
                self.stdscr.addstr(2, 3, menu['title'], curses.A_BOLD)
                self.stdscr.addstr(4, 3, menu['subtitle'], curses.A_NORMAL)
                self.stdscr.addstr(termy - 2, termx - 9, 'v' + __version__,
                                   curses.A_BOLD)
                self.stdscr.refresh()

                for index in range(optioncount):
                    textstyle = self.normal
                    if pos == index:
                        textstyle = self.highlight
                    if 'ip_addr' in menu['options'][index]:
                        pad.addstr(index, 0, '%d - %s' % (
                            index + 1, menu['options'][index]['title'] + ': ' +
                            menu['options'][index]['ip_addr']), textstyle)
                    else:    
                        pad.addstr(index, 0, '%d - %s' % (
                            index + 1, menu['options'][index]['title']),
                            textstyle)

                textstyle = self.normal
                if pos == optioncount:
                    textstyle = self.highlight
                pad.addstr(optioncount, 0, '%d - %s' %
                           (optioncount + 1, lastoption), textstyle)

                pad.refresh(scroller, 0, top, left, termy - 3, width)

            cmd = self.stdscr.getch()

            if cmd == curses.KEY_RESIZE:
                self.stdscr.erase()
                termy, termx = self.stdscr.getmaxyx()
                viewport = termy - 8
                width = termx - 4
                self.stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
                self.stdscr.addstr(1, 2, 'NetOps Jumpbox', curses.A_UNDERLINE)
                self.stdscr.addstr(2, 3, menu['title'], curses.A_BOLD)
                self.stdscr.addstr(4, 3, menu['subtitle'], curses.A_NORMAL)
                self.stdscr.addstr(termy - 2, termx - 9, 'v' + __version__,
                                   curses.A_BOLD)
                self.stdscr.refresh()
                pad.refresh(scroller, 0, top, left, termy - 3, width)

            if optioncount + 1 > viewport:
                if cmd == curses.KEY_DOWN:
                    if pos < optioncount and scroller < height - viewport:
                        pos += 1
                        scroller += 1
                    elif pos < optioncount and scroller == height - viewport:
                        pos += 1
                    elif pos == optioncount:
                        pos = 0
                        scroller = 0

                elif cmd == curses.KEY_UP:
                    if pos > 0 and scroller > 0:
                        pos -= 1
                        scroller -= 1
                    elif pos > 0 and scroller == 0:
                        pos -= 1
                    elif pos == 0:
                        pos = optioncount
                        scroller = height - viewport

                elif cmd == curses.KEY_RIGHT:
                    cmd = ord('\n')

                elif cmd == curses.KEY_LEFT:
                    pos = optioncount
                    cmd = ord('\n')

            else:
                if cmd == curses.KEY_DOWN:
                    if pos < optioncount:
                        pos += 1
                    else:
                        pos = 0

                elif cmd == curses.KEY_UP:
                    if pos > 0:
                        pos -= 1
                    else:
                        pos = optioncount

                elif cmd == curses.KEY_RIGHT:
                    cmd = ord('\n')

                elif cmd == curses.KEY_LEFT:
                    pos = optioncount
                    cmd = ord('\n')

        return pos
