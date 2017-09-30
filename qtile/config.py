import subprocess, shlex
from libqtile.config import Key, Screen, Group, Match, Drag
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

theme = 'dark'

mod = 'mod4'

keys = [
    Key([mod], 'Return', lazy.spawn('xterm tmux')),
    Key([mod], 'Tab', lazy.next_layout()),
    Key([mod], 'p', lazy.spawncmd()),
    Key([mod, 'shift'], 'Tab', lazy.layout.flip()),
    Key([mod], 'w', lazy.window.kill()),
    Key([mod, 'shift'], 'q', lazy.shutdown()),
]

_groups = {
    '1' : None,
    '2' : None,
    '3' : [Match(wm_class=['Inkscape', 'Gimp'])],
    '4' : None,
    '5' : [Match(wm_class=['Wireshark'])],
    '6' : None,
    '7' : None,
    '8' : None,
    '9' : [Match(wm_class=['Firefox'])]
}

groups = []
for label, matches in sorted(_groups.items()):
    groups.append(Group(label, matches=matches))
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], label, lazy.group[label].toscreen()),
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, 'shift'], label, lazy.window.togroup(label)),
    ])
    
layouts = [
    layout.Max(),
    layout.Stack(num_stacks=2)
]

defaults = dict(
    padding=8
)

button = 'start.png'

if theme == 'light':
    defaults.update(dict(
        background='c3c3c3',
        foreground='000000',
    ))
elif theme == 'dark':
    button = 'start_inv.png'
    defaults.update(dict(
        background='3c3c3c',
        foreground='ff8800',
    ))

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Image(filename='~/.config/qtile/' + button),
                widget.Prompt(
                    prompt='> ',
                    font='FreeMono',
                    fontsize=24,
                    cursor_color='dddd00',
                    **defaults
                ),
                widget.WindowName(
                    font='FreeMono Oblique',
                    fontsize=22,
                    **defaults
                ),
                widget.Clock(
                    format='%H:%M',
                    font='FreeMono',
                    fontsize=26,
                    **defaults
                ),
            ],
            48,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
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
    run('xterm tmux')
    
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
