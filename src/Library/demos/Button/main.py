import workbench

button_ids = [
  "regular",
  "flat",
  "suggested",
  "destructive",
  "custom",
  "disabled",
  "circular-plus",
  "circular-minus",
  "pill",
  "osd-left",
  "osd-right",
]

def onClicked(button):
  print(f"{button.get_name()} clicked")

for id in button_ids:
  button = workbench.builder.get_object(id)
  button.connect("clicked", onClicked)
