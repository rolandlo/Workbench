import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import workbench

radio_button_1 : Gtk.CheckButton = workbench.builder.get_object("radio_button_1")
radio_button_2 : Gtk.CheckButton = workbench.builder.get_object("radio_button_2")

def onModeToggled(radio_button, mode):
  if radio_button.get_active():
    print(f"Force {mode} Mode")


radio_button_1.connect("toggled", onModeToggled, "Light")
radio_button_2.connect("toggled", onModeToggled, "Dark")
