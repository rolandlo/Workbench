import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import workbench

buttons = {
  "button_no_look" : "Don't look",
  "button_look"  : "Look",
  "button_camera" : "Camera",
  "button_flashlight" : "Flashlight",
  "button_console" : "Console",
}

for id, name in buttons.items():
  button : Gtk.ToggleButton = workbench.builder.get_object(id)
  button.connect("notify::active",
    lambda button, state, name : print(f"{name} {'On' if button.get_active() else 'Off'}"),
    name
  )
