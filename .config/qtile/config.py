################
# QTILE CONFIG #
################

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os


mod = "mod4"
terminal = "urxvt"

keys = [
    # Switch between windows
    Key([mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"),
    Key([mod], "l", 
        lazy.layout.right(), 
        desc="Move focus to right"),
    Key([mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"),
    Key([mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"),
    Key([mod], "space", 
        lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", 
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", 
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", 
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", 
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"),
    Key([mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"),

    # Launch applications:
    Key([mod], "d",
        lazy.spawn("rofi -show drun"),
        desc="Launch rofi"),
    Key([mod, "shift"], "Return", 
        lazy.spawn("firefox"),
        desc="Launch firefox"),
    Key([mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"),
    Key([mod], "w", 
        lazy.window.kill(), 
        desc="Kill focused window"),

    Key([mod, "shift"], "r", 
        lazy.restart(), 
        desc="Restart Qtile"),
    Key([mod, "shift"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile")
    ]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

colors={
    "foreground":"#ffffff",
    "background":"#222222",
    "red":"#cc342b",
    "blue":"#3971ed",
    "green":"#198844",
    "cyan":"#3971ed",
    "magenta":"#a36ac7",
    "yellow":"#fba922"
    }

layout_default={
    "margin":8,
    "border_focus":colors["yellow"],
    "border_normal":'#444444',
    "border_width":2
        }
layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(
        name="MAX"),
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        name="BSP",
        **layout_default),
    # layout.Matrix(),
    layout.MonadTall(
        name="TALL",
        **layout_default),
    layout.MonadWide(
        name="WIDE",
        **layout_default),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Fira Code Medium',
    fontsize=10,
    padding=3,
    foreground=colors["foreground"]
)
extension_defaults = widget_defaults.copy()



screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=colors["foreground"],
                    borderwidth=3,
                    font='Fira Code Medium',
                    fontsize=10,
                    highlight_color=colors["green"],
                    highlight_method="line",
                    padding=3),
                widget.WindowName(
                    foreground=colors["blue"],
                    font='Fira Code Medium',
                    fontsize=10,
                    padding=5),
                widget.Spacer(),
                widget.TextBox(
                       text = '',
                       background = colors['background'],
                       foreground = colors['blue'],
                       padding = 0,
                       fontsize = 37
                       ),
                widget.CurrentLayout(
                    background=colors["blue"],
                    font='Fira Code Medium',
                    fontsize=10,
                    padding=5),
                widget.TextBox(
                       text = '',
                       background = colors['blue'],
                       foreground = colors['green'],
                    padding = 0,
                    fontsize = 37
                    ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background=colors["green"],
                    font='Fira Code Medium',
                    fontsize=10,
                    padding=5),
                widget.TextBox(
                    text = '',
                    background = colors['green'],
                    foreground = colors['blue'],
                    padding = 0,
                    fontsize = 37
                    ),
                widget.Systray(
                    padding=5,
                    background=colors["blue"]
                    ),
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=colors['blue']
                    ),
                widget.TextBox(
                    text = '',
                    background = colors['blue'],
                    foreground = colors['red'],
                    padding = 0,
                    fontsize = 37
                    ),
                widget.QuickExit(
                    default_text=" LOGOUT ",
                    background=colors["red"],
                    font='Fira Code Medium',
                    fontsize=10,
                    padding=5),
            ],
            20,
            background=colors["background"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    Match(wm_type='utility'),
    Match(wm_type='notification'),
    Match(wm_type='toolbar'),
    Match(wm_type='splash'),
    Match(wm_type='dialog'),
    Match(wm_class='file_progress'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
