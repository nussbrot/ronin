# -*- coding: utf-8 -*-
#
# Copyright 2016-2018 Tal Liron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals
from .unicode import to_str
import colorama, atexit


colorama.init()

def _restore_terminal():
    colorama.deinit()
    
atexit.register(_restore_terminal)

colors = {
    'green': colorama.Fore.GREEN,
    'red': colorama.Fore.RED,
    'yellow': colorama.Fore.YELLOW,
}
reset_color = colorama.Style.RESET_ALL


def announce(message, prefix='rōnin', color='green'):
    """
    Writes a message to the terminal with a colored prefix.
    
    :param message: message
    :type message: str
    :param color: color name
    :type color: str
    """

    if color and color in colors:
        prefix = colors[color] + prefix + reset_color
    print('{}: {}'.format(prefix, message))


def error(message):
    """
    Writes an error message to the terminal with a red prefix.
    
    :param message: message or exception
    :type message: str or BaseException subclass instance
    """
    
    if isinstance(message, BaseException):
        the_type = type(message).__name__
        message = to_str(message)
        if message:
            announce('{}: {}'.format(the_type, message), color='red')
        else:
            announce(the_type, color='red')
    else:
        announce('Error: {}'.format(message), color='red')


def warning(message):
    """
    Writes a warning message to the terminal with a yellow prefix.
    
    :param message: message
    :type message: str
    """

    announce('Warning: {}'.format(message), color='yellow')
