# HwaeTILE

QTile is a tiling window manager written in Python.  Out the box on first load under default configuration, it shows unusual sexiness.  HwaeTILE extends the default configuration of QTile, providing an easier to use interface and features more common to desktop environment, while preserving the awesome workflow that comes from tiling window managers.

The purpose of HwaeTILE is to provide users with a more developed and usable default config for QTile.  From which they might choose to either use as is or furhter develop to suit their particular needs.


## Current Development

**Version 0.1**: For the initial release, the development goals are to provide the base interface system for HwaeTILE.  It supports QTile version 0.8, which is written in Python 2.7.  It will use GTK+ version 3, using PyGObject.

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
  - System Monitor
  - Battery
  - Time Zone
- Implement notification system.
- Implement support for Numix icons
- Implement dock


## Known Issues

These are the current bugs and known issues:

- When HwaeTILE launches, the `autostart()` function blanks out the top panel when it launches my cloud sync client.  For the moment it is not clear why, so I would welcome any suggestions.  Clicking `Mod4` + `r` to launch the prompt on the top panel seems to update the rendering to restore it.

- When HwaeTILE launches, the cusror starts invislbe.  You can restore it by opening a window, for instance `Mod4` + `Return` to launch `xterm`.  The reason for this is also not clear.  I suspect it may relate to what happens to the top panel in the aforementioned issue.




## Releases Notes

None.  Inital version still in development.



