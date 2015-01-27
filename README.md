# HwaeTILE

QTile is a tiling window manager written in Python.  Out the box on first load under default configuration, it shows unusual sexiness.  HwaeTILE extends the default configuration of QTile, providing an easier to use interface and features more common to desktop environment, while preserving the awesome workflow that comes from tiling window managers.

The purpose of HwaeTILE is to provide users with a more developed and usable default config for QTile.  From which they might choose to either use as is or furhter develop to suit their particular needs.


## Current Development

For the initial release, the development goals are to provide the base interface system for HwaeTILE.  It supports QTile version 0.8, which is written in Python 2.7.  It will use GTK+ version 3, using PyGObject.

- Implement client decorations.
- Implement panel menus, similar to Gnome 3.
  - Prompt
  - Application Menu
  - Volume
  - Weather
  - System Monitor
  - Battery
  - Calendar
  - Todo
- Implement panel widgets
  - Battery
  - Time Zone
- Implement notification system.
- Implement support for Numix icons
- Implement dock


## Known Issues

These are the current bugs and known issues:

- When HwaeTILE launches, the `autostart()` function blanks out the top panel when it launches my cloud sync client.  For the moment it is not clear why, so I would welcome any suggestions.  Clicking `Mod4` + `r` to launch the prompt on the top panel seems to update the rendering to restore it.

- When HwaeTILE launches, the cusror starts invislbe.  You can restore it by opening a window, for instance `Mod4` + `Return` to launch `xterm`.  The reason for this is also not clear.  I suspect it may relate to what happens to the top panel in the aforementioned issue.

- The keyboard configurations should call the `synclient()` function in reponse to `Mod4 + XF86LaunchA` or `Super + F4` on my Macbook, but does not.  Reason not yet clear.


## Releases Notes

### Version 0.1

Initial dev release.  Not exactly stable, little wonky, but it works well enough for use while I fix other things.

Features:

- Created a top and bottom panels, populated with various widgets.

- Implemented a number of widgets, including a system monitor, a count of available packages for update through `pacman`, a textbox that shows the current tiling layout.

- Developed a prototype for toggling the touchpad, which can be found in the `scripts/` directory.  The function for this prototype is included in the `config.py` file, but is not yet usable.

- Maintained the default group scheme (called workspaces in desktop environments), though expanded it for window matching.  The letters in the display indicate those you press with `Mod4` to switch to that group.



