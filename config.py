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

# Mouse Configuration
mouse = [
    Drag ( [ mod ], "Button1",
           lazy.window.set_position_floating(),
           start = lazy.window.get_position() ),
    Drag ( [ mod ], "Button3",
           lazy.window.set_size_floating(),
           start = lazy.window.get_size() ),
    Clock ( [ mod ], "Button2",
            lazy.window.bring_to_front() )

]

