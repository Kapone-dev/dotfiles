from libqtile.config import Screen
from libqtile.bar import Bar

from settings.widgets import groups_widgets

screens = [
    Screen(
        top=Bar(
            groups_widgets,
            28,
        ),
    ),
]