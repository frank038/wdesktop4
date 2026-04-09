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
- desktop files support (programs)
- supports the command line arguments trash:// (the recycle bin) and media://DEVICE (mass storage devices) of my file manager SimpleFM6
- applications can be dropped from the menu of my wbar4
- folder custom icon support
- can load a custom script to render something in the background using cairo; a sample script is provided; enable or disable it with the center mouse button
- widgets.

About widgets: custom widgets can be created in the folder widgets; two sample widgets, a calendar and a note taking, are provided as reference; to load them just use the center mouse button and press the entry 'Widgets': a dialog will appear; after selecting one name some infos and actions will appear; the same procedure for removing them; the widgets can be moved with the right mouse button and resized with the center mouse button (with some limitations in the size).

Do not support multi monitors. May have some unknown issues.
