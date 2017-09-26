import subprocess, shlex
from libqtile.config import Key, Screen, Group, Match, Drag
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

mod = "mod4"

keys = [
    Key([mod], "Return", lazy.spawn("xterm")),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "p", lazy.spawncmd()),
    Key([mod, "shift"], "Tab", lazy.layout.flip()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "shift"], "q", lazy.shutdown()),
]

groups = [Group(str(i)) for i in range(1, 10)]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

groups[2].matches = [Match(wm_class=["Inkscape", "GIMP"])]
groups[4].matches = [Match(wm_class=["Wireshark"])]
groups[8].matches = [Match(wm_class=["Firefox"])]
    
layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

defaults = dict(
    font='DeJaVu Sans Mono',
    fontsize=30,
    background='c3c3c3',
    foreground='000000',
)

insane_defaults = defaults.copy()
insane_defaults['background'] = 'ffff00'

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Image(filename='~/.config/qtile/start.png'),
                widget.GroupBox(
                    active='000000',
                    borderwidth=0,
                    inactive='707070',
                    rounded=False,
                    padding=6,
                    highlight_method='line',
                    highlight_color=['ff0000', '00ff00'],
                    **defaults
                ),
                widget.Prompt(
                    prompt='>',
                    cursor_color='dd4400',
                    **insane_defaults
                ),
                widget.TextBox(width=bar.STRETCH, **defaults),
                widget.Clock(format='%Y-%m-%d %a %H:%M', **defaults),
            ],
            48,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
]

def run(cmd):
    try:
        subprocess.Popen(shlex.split(cmd))
    except:
        pass

@hook.subscribe.startup
def startup():
    run('firefox')
    run('xterm')
    
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
