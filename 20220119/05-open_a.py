#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

archivo = open("demo2.txt", "a")

archivo.write("Linea 1")
archivo.write(" Linea 2")
archivo.write(" Linea 3")

archivo.close()
