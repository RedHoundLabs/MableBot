import gtk

format = "jpeg"

width = gtk.gdk.screen_width()
height = gtk.gdk.screen_height()
screenshot = gtk.gdk.Pixbuf.get_from_drawable(
          gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, True, 8, width, height),
          gtk.gdk.get_default_root_window(),
          gtk.gdk.colormap_get_system(),
          0, 0, 0, 0, width, height)

# Pixbuf's have a save method
# Note that png doesnt support the quality argument.
screenshot.save("screenshot." + format, format,  {"quality": "20"})
