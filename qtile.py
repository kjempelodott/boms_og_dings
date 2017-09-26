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

groups[8].matches = [Match(wm_class=["Firefox"])]
    
layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='DejaVu Sans Mono',
    fontsize=16,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %H:%M'),
            ],
            30,
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
