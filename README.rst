######
README
######

HwaeTILE provides initialization files for several tiling window managers.
Its purpose is to provide the user with an advanced configuration to either
use as is or to provide guidance in developing their own environments.  Below,
you'll find a list of the supported window managers and the paths the Org file
writes to.  If you have an existing window manager configuration at these paths,
you should change the filename.  For instance, with i3wm:

.. code-block:: console

   mv ~/.config/i3/config ~/.config/i3/config-old

Below you'll find a list of the supported window managers and the paths they tangle to:

Supported Window Managers:

- **i3wm**: ``~/.config/i3/config``

.. note:: Tangle writes are all relative to the home directory.  You can redirect
          them by temporarily changing the ``$HOME`` environmental variable:

          .. code-block:: console

             $ export HOME=/path/to/temporary_dir

          After tangling, run the same command, resetting ``$HOME`` back to your
          ``/home`` path or rebooting.
