# wdesktop4
An application that manages the desktop.

Requirements:
- python3
- gtk4 binding
- Gtk4LayerShell (optional but recommended)
- psutil (optional, for storage devices)
- PIL (optional, for thumbnailers)
- pdftocairo (optional, for the pdf thumbnailer)
- ffmpegthumbnailer (optional, for the video thumbnailer)
- wayland (maybe should work also under xorg).
- a window manager that support the layer shell protocol (if enabled)

Features:
- main file operations
- drag and drop support
- copy/cut/paste support
- recycle bin support
- storage devices support
- rubberband
- track the change of the icon theme
- a separated language file 
- options in its config file
- some service scripts for a terminal and a file manager (to be setted by the user)
- left mouse button for each item operations
- right mouse button for some operations
- center mouse button for other functions
- easy creation of more thumbnailers
- desktop files support (programs).

Do not support multi monitors. May have some unknown issues.
