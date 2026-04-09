
# the exactly same name of the main directory of this module
_MODULE="Calendar"
# module data
_NAME="Calendar"
_VERSION="Version 1.0"
_COMMENT="Just a calendar"
_DATA="Sample widget"

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Gdk', '4.0')
from gi.repository import Gtk, GLib, Gdk, Gio, Graphene
import os

class customWidget(Gtk.Widget):
    def __init__(self, _parent, _path, _width, _height):
        super().__init__()
        self._parent = _parent
        self._path = _path
        self._width =_width
        self._height =_height
        self._name = _NAME
        self._module = _MODULE
        #
        self._style_context = self.get_style_context()
        # custom name for the css
        self._style_context.add_class("wcalendar")
        css_provider = Gtk.CssProvider()
        css_provider.load_from_file(Gio.File.new_for_path(self._path+'/widgetstyle.css'))
        Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        # vertical box
        self.main_box = Gtk.Box.new(1,0)
        #
        _l = Gtk.BoxLayout.new(1)
        self.set_layout_manager(_l)
        #
        self.main_box.set_parent(self)
        ########### widget content ###########
        self._populate()
        ######### end widget content #########
        # right mouse button - selection
        self.da_gesture_l = Gtk.GestureClick.new()
        self.da_gesture_l.set_button(3)
        self.add_controller(self.da_gesture_l)
        # self.da_gesture_l.connect('pressed', self.on_da_gesture_l, 1)
        self.da_gesture_l.connect('released', self.on_da_gesture_l, 0)
        # center mouse button - resize
        self.da_gesture_c = Gtk.GestureClick.new()
        self.da_gesture_c.set_button(2)
        self.add_controller(self.da_gesture_c)
        self.da_gesture_c.connect('pressed', self.on_da_gesture_c)
        self.da_gesture_c.connect('released', self.on_da_gesture_cr)
        # right mouse button - dragging
        self.da_gesture_d = Gtk.GestureDrag.new()
        self.da_gesture_d.set_button(3)
        self.add_controller(self.da_gesture_d)
        self.da_gesture_d.connect('drag-update', self.on_da_gesture_d_u)
        # center mouse button - dragging
        self.da_gesture_c = Gtk.GestureDrag.new()
        self.da_gesture_c.set_button(2)
        self.add_controller(self.da_gesture_c)
        self.da_gesture_c.connect('drag-update', self.on_da_gesture_c_u)
        #
        self._x = 0
        self._y = 0
        self._fixed_width = 0
        self._fixed_height = 0
        self.self_width = 0
        self.self_height = 0
    
    def _populate(self):
        self._calendar = Gtk.Calendar.new()
        self._calendar.set_vexpand(True)
        self.main_box.append(self._calendar)
    
    def on_da_gesture_c(self, o,n,x,y):
        _point = Graphene.Point()
        _point.x = int(x)
        _point.y = int(y)
        ret_point = self.compute_point(self._parent._fixed, _point)
        if ret_point[0] == True:
            self._x = int(ret_point[1].x)
            self._y = int(ret_point[1].y)
    
    def on_da_gesture_cr(self, o,n,x,y):
        _x1 = self._x
        _y1 = self._y
        try:
            with open(os.path.join(self._path,"locationcfg"), "w") as _f:
                _f.write("{}\n{}\n{}\n{}".format(_x1,_y1, self.get_allocated_width(), self.get_allocated_height()))
        except:
            pass
        self.self_width = 0
        self.self_height = 0
        self._fixed_width = 0
        self._fixed_height = 0
    
    def on_da_gesture_c_u(self, gesture_drag, offset_x, offset_y):
        if self.self_width == 0:
            self.self_width = self.get_allocated_width()
        if self.self_height == 0:
            self.self_height = self.get_allocated_height()
        if self._fixed_width == 0:
            self._fixed_width = self._parent._fixed.get_width()
        if self._fixed_height == 0:
            self._fixed_height = self._parent._fixed.get_height()
        _w = self.self_width+offset_x
        _h = self.self_height+offset_y
        if offset_x > 0 and (self._x +self.get_allocated_width() >= (self._fixed_width-10)):
            return
        if offset_y > 0 and (self._y +self.get_allocated_height() >= (self._fixed_height-10)):
            return
        if _w > int(self._fixed_width/2) or _w < 40:
            return
        if _h > int(self._fixed_height/2) or _h < 40:
            return
        self.set_size_request(_w,_h)
        
    def on_da_gesture_d_u(self, gesture_drag, offset_x, offset_y):
        if self._fixed_width == 0:
            self._fixed_width = self._parent._fixed.get_width()
        if self._fixed_height == 0:
            self._fixed_height = self._parent._fixed.get_height()
        _point = Graphene.Point()
        _point.x = offset_x
        _point.y = offset_y
        ret_point = self.compute_point(self._parent._fixed, _point)
        if ret_point[0] == True:
            self._x = int(ret_point[1].x)
            self._y = int(ret_point[1].y)
            if self._x < 0:
                self._x = 10
            if self._y < 0:
                self._y = 10
            if self._x+self.get_allocated_width() > self._fixed_width:
                self._x = self._fixed_width-self.get_allocated_width()-10
            if self._y+self.get_allocated_height() > self._fixed_height:
                self._y = self._fixed_height-self.get_allocated_height()-10
            self._parent._fixed.move(self, self._x, self._y)
    
    def on_da_gesture_l(self, o,n,x,y, _t):
        _x1 = self._x
        _y1 = self._y
        try:
            with open(os.path.join(self._path,"locationcfg"), "w") as _f:
                _f.write("{}\n{}\n{}\n{}".format(_x1,_y1, self._width, self._height))
        except:
            pass
        self._x = 0
        self._y = 0
        self._fixed_width = 0
        self._fixed_height = 0
        