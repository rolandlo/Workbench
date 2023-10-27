import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import workbench

hours : Gtk.SpinButton = workbench.builder.get_object("hours")
minutes : Gtk.SpinButton = workbench.builder.get_object("minutes")

hours.set_text("00")
minutes.set_text("00")

def tellTime(hours, minutes):
  return f"The time selected is {hours.get_text()}:{minutes.get_text()}"

hours.connect("value-changed", 
  lambda _ : print(tellTime(hours, minutes))
)
minutes.connect("value-changed", 
  lambda _ : print(tellTime(hours, minutes))
)

def onTimeChanged(spin_button):
  value = int(spin_button.get_adjustment().get_value())
  text = str(value).rjust(2, "0")
  spin_button.set_text(text)
  return True

hours.connect("output", onTimeChanged)
minutes.connect("output", onTimeChanged)

# This only works for one direction
# Add any extra logic to account for wrapping in both directions
minutes.connect("wrapped",
  lambda _ : hours.spin(Gtk.SpinType.STEP_FORWARD, 1)
)
