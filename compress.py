#!/usr/bin/env python

import gi
gi.require_version('GCab', '1.0')
from gi.repository import GCab
from gi.repository import Gio

def compress(src_path, dest_path):
    cab_file = GCab.File.new_with_file(src_path,
                                       Gio.File.new_for_path(src_path))

    cab_folder = GCab.Folder.new(GCab.Compression.MSZIP)
    cab_folder.add_file(cab_file, False)

    cab = GCab.Cabinet.new()
    cab.add_folder(cab_folder)

    out_file = Gio.File.new_for_path(dest_path)
    cab.write_simple(out_file.replace(None,
                                      False,
                                      Gio.FileCreateFlags.REPLACE_DESTINATION,
                                      None))


compress("some.file", "some.file.cab")