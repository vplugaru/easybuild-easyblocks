##
# This file is an EasyBuild reciPY as per https://github.com/hpcugent/easybuild
#
# Copyright:: Copyright 2012-2013 University of Luxembourg/Luxembourg Centre for Systems Biomedicine
# Authors::   Fotis Georgatos <fotis.georgatos@uni.lu>
# License::   MIT/GPL
# $Id$
#
# This work implements a part of the HPCBIOS project and is a component of the policy:
# http://hpcbios.readthedocs.org/en/latest/HPCBIOS_06-05.html
##
"""
EasyBuild support for installing Totalview, implemented as an easyblock

@author: Fotis Georgatos (Uni.Lu)
"""
import os

from easybuild.framework.easyblock import EasyBlock
from easybuild.tools.filetools import run_cmd
from easybuild.tools.modules import get_software_root

class EB_TotalView(EasyBlock):
    """EasyBlock for TotalView"""

    def configure_step(self):
        """No configuration for TotalView."""

        pass

    def build_step(self):
        """No building for TotalView."""

        pass

    def install_step(self):
        """Custom install procedure for TotalView."""

        cmd = "./Install -agree -platform linux-x86-64 -nosymlink -install totalview -directory %s" % self.installdir
        run_cmd(cmd)

    def sanity_check_step(self):
        """Custom sanity check for TotalView."""

        binpath_t = 'toolworks/%s.%s/bin/' % ('totalview', self.version) + 'tv%s'

        custom_paths = {
                              'files': [binpath_t % i for i in ['8', '8cli', 'dbootstrap', 'dsvr', 'script']],
                              'dirs': []
                             }

        super(EB_TotalView, self).sanity_check_step(custom_paths=custom_paths)
