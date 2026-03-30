# use the layershell protocol: 1 yes - 0 no
USE_LAYERSHELL = 1
# wayland layer: 0 bottom - 1 background
LAYER_PLACEMENT = 1
# reduce the width of the window (useful for vertical panels with exclusive zones)
SCREEN_SHRINK_W = 0
# reduce the height of the window (useful for horizontal panels with exclusive zones)
SCREEN_SHRINK_H = 0
# the desktop folder: 1 default - or type the full path for other location
DESKTOP_PATH = 1
# BORDER MARGINS: pixels
TOP_MARGIN = 0
BOTTOM_MARGIN = 0
LEFT_MARGIN = 20
RIGHT_MARGIN = 0
# desktop item size: pixels
DESKTOP_ITEM_SIZE = 148
# space between icon and text: pixels
ICON_TEXT_SEPARATOR = 10
# space between items - item internal: pixels
ITEM_MARGIN = 8
ITEM_MARGIN_V = 8
# item placement: 0 top to bottom - 1 left to right
ITEM_PLACEMENT = 0
# icon size - square: pixels
w_icon_size = 64
# font family: name
font_fm = "Sans"
# item font size - 0 default - or size
font_font_size = 0
# corner radius of the text background
ROUNDED_CORNER = 3
# number of lines of each item text
NUMBER_OF_TEXT_LINES = 2
# the text colour: normal and highlight states
TEXT_NORMAL_COLOR = "#000000"
TEXT_HIGHLIGHT_COLOR = "#000000"
# normal text background colour
TEXT_BACKGROUND_NORMAL = "#aaaaaaaa"
# highlight text background colour
TEXT_BACKGROUND_HIGHLIGHT = "#88ccffaa"
## emplems
EMBLEM_SIZE = 30
THICK_SIGN = "✓"
THICK_SIGN_SIZE = 10
THICK_COLOR = "#ffffffff"
THICK_PAD = 2
# use the recycle bin
USE_TRASH = 1
TRASH_NAME = "Recycle bin"
# trash position: 0 bottom right - 1 top right - 2 bottom left - 3 top left
TRASH_POSITION = 0
# use the thumbnailers
USE_THUMBS = 1
# custom folder for thumbnails: 1 custom - 0 system (in .cache directory)
THUMB_CUSTOM_FOLDER = 1
# use the storage devices
USE_MEDIA = 1
# list of device do not track: e.g. ["/dev/sda1", "/dev/sda2"]
MEDIA_SKIP = []
## rubberband
# the border width
R_LINE_WIDTH = 1
# the border color
R_BORDER_COLOR = "#00000088"
# the inside color
R_COLOR = "#88ccff20"
# corner radius
R_RADIUS = 6
# background: 0 image - 1 colour - 2 none (transparet background)
# image name - mandatory name: wallpaper.png
USE_BACKGROUND_COLOR = 2
BACKGROUND_COLOR = "#777777"
# the folder to copy in the desktop already exists: 0 rename - 1 merge
FOLDER_MERGE = 1
# button label alignment: 0 left - 1 right
BUTTON_LABEL_ALIGN=0
# maximum number of icons to show while dragging: 0 all - or number
THUMB_DRAG_MAX = 0
# size of the icons while dragging: pixels
THUMB_DRAG_ICON_SIZE = 32