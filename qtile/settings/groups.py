from libqtile.config import Group, Key
from libqtile.lazy import lazy

from settings.keys import keys, mod

groups = [Group(i) for i in [" 爵 ", "  ", "  ", "  ", "  ", " ﭮ " ,"  "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True)),
    ])