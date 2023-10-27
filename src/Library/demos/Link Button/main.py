import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import workbench

linkbutton : Gtk.LinkButton = workbench.builder.get_object("linkbutton")

linkbutton.connect("notify::visited", 
  lambda _ : print("The link has been visited")
)

def activateLink(button):
  print(f"About to activate {button.get_uri()}")
  # Return True if handling the link manually, or
  # False to let the default behavior continue
  return False

linkbutton.connect("activate-link", activateLink)
