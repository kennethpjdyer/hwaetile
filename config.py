#########################################################
# config.py - Default configuration file for Hwaetile,  #
#  an extension of the tiling window manager QTile. To  #
#  use, place this file at ~/.config/qtile/, then add   #
#  exec qtile to your .xinit.                           #
#########################################################


###########################
# Module Imports
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
import os, subprocess

##########################
# Default Variables

# Terminal
term = "xterm"

# Modifier Key
mod = "mod4"


#########################
# Layout Configuration
layouts = [
    layout.MonadTall(),
    layout.Matrix(),
    layout.Tile(),
    layout.VerticalTile(),
    layout.Stack(num_stacks=2),
    layout.Max()
]

########################
# Group Configuration
groups = [
    # Main Group
    Group ( "a"),
    
    # Emacs Group
    Group ( "s"),

    # Office Group
    Group ( "d"),

    # Media Group
    Group ( "f"),

    # ext5
    Group ( "u" ),

    # ext6
    Group ( "i" ),

    # ext7
    Group ( "o" ),

    # ext8
    Group ( "p" ),
]


##########################
# Widget Configurations
widget_defaults = dict (
    font = "Arial",
    fontsize = 14,
    padding = 3,
)

# Clock and Calendar Configurations
clock = "%I:%M %p"
calendar = "%I"


# Top Panel Configuration

battery = ''

topleft = [
    widget.TextBox( "Launcher", name = "launch" ),
    widget.Prompt(),
    widget.Spacer( width = 5 ),
    widget.WindowName(),
]

graphwidth = 25
topright = [
    widget.CPUGraph( core = 0, width = graphwidth ),
    widget.CPUGraph( core =1, width = graphwidth ),
    widget.MemoryGraph( width = graphwidth ),
    widget.SwapGraph( width = graphwidth ),
    widget.NetGraph( width = graphwidth ),
    widget.Systray(),
    widget.Clock( format = clock ),
]

toppanel = topleft + topright


# Bottom Panel Configuration
botleft = [
    widget.GroupBox(),
    widget.TaskList(),
]

botright = [
    widget.Pacman(update_interval = 60 ),
    widget.Clock ( format = clock ),
    widget.CurrentLayout(),
]

botpanel = botleft + botright


# Build Screens
screens = [
    Screen (
        top = bar.Bar( toppanel, 30, ),
        bottom = bar.Bar( botpanel, 30, ),
    )
]

# General Configuration
dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True

# Java Trolling
wmname = "LG3D"




##########################
# Keyboard Configuration
keys = [
    # Switch Windows in Current Stack Pane
    Key( [ mod ], "j",
         lazy.layout.down() ),
    Key( [ mod ], "k",
         lazy.layout.up() ),

    # Move Window in Current Stack
    Key( [ mod, "shift" ], "j",
         lazy.layout.shuffle_down() ),
    Key( [ mod, "shift" ], "k",
         lazy.layout.shuffle_up() ),

    # Switch Focus to other Pane
    Key( [ mod ], "space",
         lazy.layout.next() ),

    # Swap Panes of Split Stack
    Key( [ mod, "shift" ], "space",
         lazy.layout.rotate() ),

    # Toggle Split and Unsplit Stack
    Key( [ mod, "shift" ], "Return",
         lazy.layout.toggle_split() ),

    # Open Terminal
    Key( [ mod ], "Return",
         lazy.spawn(term) ),

    # Layout Toggle
    Key ( [ mod ], "Tab",
         lazy.nextlayout() ),
    Key ( [ mod, "shift" ], "Tab",
          lazy.prevlayout() ),

    # Kill Window
    Key ( [ mod ], "w",
          lazy.window.kill() ),

    # Start and Restart Hwaetile
    Key ( [ mod, "shift" ], "r",
          lazy.restart() ),
    Key ( [ mod, "shift" ], "q",
          lazy.shutdown() ),

    # Open Command Prompt
    Key ( [ mod ], "r",
          lazy.spawncmd() ),
    
]

# Set Groups
for i in groups:
    keys.append (
        Key ( [ mod ], i.name,
              lazy.group[i.name].toscreen())
        )
    keys.append (
        Key ( [ mod, "shift" ], i.name,
              lazy.window.togroup(i.name)),
    )

# Mouse Configuration
mouse = [
    Drag ( [ mod ], "Button1",
           lazy.window.set_position_floating(),
           start = lazy.window.get_position() ),
    Drag ( [ mod ], "Button3",
           lazy.window.set_size_floating(),
           start = lazy.window.get_size() ),
    Click ( [ mod ], "Button2",
            lazy.window.bring_to_front() )

]


#################################
# Hook Configurations

# Autostart Call
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.call([home + '/.config/qtile/autostart.sh'])
