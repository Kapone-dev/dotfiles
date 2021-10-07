from typing import List # noqa: F401

from libqtile import hook

from settings.keys import keys
from settings.groups import groups
from settings.layout import layouts, floating_layout
from settings.mouse import mouse
from settings.screens import screens
from settings.widgets import extension_defaults, widget_defaults

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
