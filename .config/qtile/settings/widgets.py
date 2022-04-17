from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


icon = lambda fg='text', bg='dark', fontsize=12, text="?": widget.TextBox(
    **base(fg, bg), fontsize=fontsize, text=text, padding=3)

powerline = lambda fg="light", bg="dark": widget.TextBox(
    **base(fg, bg),
    text="",  # Icon: nf-oct-triangle_left
    fontsize=37,
    padding=-4)

pomodoro = lambda fg='text', bg='dark', fontsize=12, text="?": widget.Pomodoro(
    **base(fg, bg),
    # **base(bg='color4'),
    padding=5)


def workspaces():
    return [
        separator(),
        widget.GroupBox(**base(fg='light'),
                        font='Anonymice Nerd Font',
                        fontsize=19,
                        margin_y=3,
                        margin_x=0,
                        padding_y=8,
                        padding_x=5,
                        borderwidth=1,
                        active=colors['active'],
                        inactive=colors['inactive'],
                        rounded=False,
                        highlight_method='block',
                        urgent_alert_method='block',
                        urgent_border=colors['urgent'],
                        this_current_screen_border=colors['focus'],
                        this_screen_border=colors['grey'],
                        other_current_screen_border=colors['dark'],
                        other_screen_border=colors['dark'],
                        disable_drag=True),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    separator(),
    #powerline('color4', 'dark'),
    #icon(bg="color4", text='祥'),  # Icon: nf-fa-download
    #pomodoro('color4', 'color4'),

    #powerline('color3', 'color4'),

    # icon(bg="color3", text=' '),  # Icon: nf-fa-feed

    #widget.Wlan(**base(bg='color3'), interface='wlp2s0'),
    #widget.Net(**base(bg='color3'), interface='wlp2s0'),
    #widget.Battery(**base(bg='color3'), update_interval=1800),
    powerline('color2', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
    widget.CurrentLayout(**base(bg='color2'), padding=5),
    # widget.PulseVolume(**base(bg='color2')),
    powerline('color1', 'color2'),
    icon(bg="color1", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    powerline('dark', 'color1'),
    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    widget.CurrentLayout(**base(bg='color1'), padding=5),
    powerline('color4', 'color1'),
    icon(bg="color4", text=' '),  # Icon: nf-fa-download
    widget.CheckUpdates(**base(bg='color4'), update_interval=1800),
]

widget_defaults = {
    'font': 'Anonymice Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy
