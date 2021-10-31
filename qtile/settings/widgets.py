from libqtile import bar, widget

from settings.theme import colors

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=29,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )



groups_widgets = [
    widget.GroupBox(
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors["active"],
        inactive=colors["inactive"],
        rounded=False,
        highlight_method='block',
        this_current_screen_border=colors["focus"],
        this_screen_border=colors["focus"]
    ),
    widget.Prompt(
        fontsize=18
    ),

    widget.WindowName(
        fontsize=14,
        max_chars=30
    ),

    powerline('color5', 'dark'),
    widget.CurrentLayout(
        background=colors["color5"],
        foreground=colors["text"],
        padding=5
    ),

    powerline('color3', 'color5'),
    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    widget.Net(
        interface="wlp4s0",
        format='{down} ↓↑ {up}',
        padding=5,
        background=colors["color3"],
        foreground=colors["text"]
    ),
    
    powerline('color4', 'color3'),
    icon(bg="color4", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color1', 'color4'),
    widget.Systray(
        background=colors["color1"]
    ),

    powerline('color2', 'color1'),
    widget.Clock(
        format='%d/%m/%y - %H:%M',
        background=colors["color2"],
        foreground=colors["text"]
    ),
]