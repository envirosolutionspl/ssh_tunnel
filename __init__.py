# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SshTunnel
                                 A QGIS plugin
 QGIS Plugin to establish a secure connection via SSH tunnel for such purposes like database connection.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-04-06
        copyright            : (C) 2020 by Michał Włoga - EnviroSolutions Sp. z o.o.
        email                : office@envirosolutions.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
import os, sys
plugin_dir = os.path.dirname(__file__)
site_package_sshtunnel = os.path.join(plugin_dir, 'libs/site-packages', 'sshtunnel')

try:
    import sshtunnel
except ImportError:
    import sys
    sys.path.append(site_package_sshtunnel)
    import sshtunnel
TunnelForwarder = sshtunnel.SSHTunnelForwarder
# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SshTunnel class from file SshTunnel.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """

    from .ssh_tunnel import SshTunnelQgis
    return SshTunnelQgis(iface)
