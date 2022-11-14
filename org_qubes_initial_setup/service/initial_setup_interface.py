#
# Copyright (C) 2020 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
import logging

from dasbus.server.interface import dbus_interface
from dasbus.server.property import emits_properties_changed
from dasbus.typing import *  # pylint: disable=wildcard-import,unused-wildcard-import

from pyanaconda.modules.common.base import KickstartModuleInterface

from org_qubes_initial_setup.constants import INITIAL_SETUP

log = logging.getLogger(__name__)


@dbus_interface(INITIAL_SETUP.interface_name)
class InitialSetupInterface(KickstartModuleInterface):
    """The interface for InitialSetup.

    The interface class is needed for interfacing code running within
    Anaconda's main process and code running in the D-Bus service process. The
    dasbus library will automatically set up a D-Bus interface based on these
    classes.
    """

    def connect_signals(self):
        super().connect_signals()
        self.watch_property("allow_usb_mouse", self.implementation.allow_usb_mouse_changed)
        self.watch_property("bool_options", self.implementation.bool_options_changed)
        self.watch_property("custom_pool", self.implementation.custom_pool_changed)
        self.watch_property("debian_available", self.implementation.debian_available_changed)
        self.watch_property("default_template", self.implementation.default_template_changed)
        self.watch_property("default_vms", self.implementation.default_vms_changed)
        self.watch_property("disp_firewallvm_and_usbvm", self.implementation.disp_firewallvm_and_usbvm_changed)
        self.watch_property("disp_netvm", self.implementation.disp_netvm_changed)
        self.watch_property("fedora_available", self.implementation.fedora_available_changed)
        self.watch_property("gui_mode", self.implementation.gui_mode_changed)
        self.watch_property("seen", self.implementation.seen_changed)
        self.watch_property("skip", self.implementation.skip_changed)
        self.watch_property("system_vms", self.implementation.system_vms_changed)
        self.watch_property("templates_aliases", self.implementation.templates_aliases_changed)
        self.watch_property("templates_to_install", self.implementation.templates_to_install_changed)
        self.watch_property("usbvm", self.implementation.usbvm_changed)
        self.watch_property("usbvm_available", self.implementation.usbvm_available_changed)
        self.watch_property("usbvm_with_netvm", self.implementation.usbvm_with_netvm_changed)
        self.watch_property("vg_tpool", self.implementation.vg_tpool_changed)
        self.watch_property("whonix_available", self.implementation.whonix_available_changed)
        self.watch_property("whonix_default", self.implementation.whonix_default_changed)
        self.watch_property("whonix_vms", self.implementation.whonix_vms_changed)

    @property
    def allow_usb_mouse(self) -> Bool:
        return self.implementation.allow_usb_mouse 

    @emits_properties_changed
    def set_allow_usb_mouse(self, allow_usb_mouse: Bool):
        self.implementation.set_allow_usb_mouse(allow_usb_mouse)

    @property 
    def bool_options(self) -> Bool:
        return self.implementation.bool_options 

    @emits_properties_changed
    def set_bool_options(self, bool_options: Bool):
        self.implementation.set_bool_options(bool_options)

    @property 
    def custom_pool(self) -> Str:
        return self.implementation.custom_pool 

    @emits_properties_changed
    def set_custom_pool(self, custom_pool: Str):
        self.implementation.set_custom_pool(custom_pool)

    @property
    def debian_available(self) -> Bool:
        return self.implementation.debian_available 

    @emits_properties_changed
    def set_debian_available(self, debian_available: Bool):
        self.implementation.set_debian_available(debian_available)

    @property 
    def default_template(self) -> Bool:
        return self.implementation.default_template 

    @emits_properties_changed
    def set_default_template(self, default_template: Bool):
        self.implementation.set_default_template(default_template) 

    @property 
    def default_vms(self) -> Bool:
        return self.implementation.default_vms 

    @emits_properties_changed
    def set_default_vms(self, default_vms: Bool):
        self.implementation.set_default_vms(default_vms)

    @property 
    def disp_firewallvm_and_usbvm(self) -> Bool:
        return self.implementation.disp_firewallvm_and_usbvm 

    @emits_properties_changed
    def set_disp_firewallvm_and_usbvm(self, disp_firewallvm_and_usbvm: Bool):
        self.implementation.set_disp_firewallvm_and_usbvm(disp_firewallvm_and_usbvm)

    @property 
    def disp_netvm(self) -> Bool:
        return self.implementation.disp_netvm 

    @emits_properties_changed
    def set_disp_netvm(self, disp_netvm: Bool):
        self.implementation.set_disp_netvm(disp_netvm)

    @property 
    def fedora_available(self) -> Bool:
        return self.implementation.fedora_available 

    @emits_properties_changed
    def set_fedora_available(self, fedora_available: Bool):
        self.implementation.set_fedora_available(fedora_available)
        
    @property 
    def gui_mode(self) -> Bool:
        return self.implementation.gui_mode 

    @emits_properties_changed
    def set_gui_mode(self, gui_mode: Bool):
        self.implementation.set_gui_mode(gui_mode)
        
    @property 
    def seen(self) -> Bool:
        return self.implementation.seen 

    @emits_properties_changed
    def set_seen(self, seen: Bool):
        self.implementation.set_seen(seen)
        
    @property 
    def skip(self) -> Bool:
        return self.implementation.skip 

    @emits_properties_changed
    def set_skip(self, skip: Bool):
        self.implementation.set_skip(skip)
        
    @property 
    def system_vms(self) -> Bool:
        return self.implementation.system_vms 

    @emits_properties_changed
    def set_system_vms(self, system_vms: Bool):
        self.implementation.set_system_vms(system_vms)

    @property 
    def templates_aliases(self) -> Bool:
        return self.implementation.templates_aliases 

    @emits_properties_changed
    def set_templates_aliases(self, templates_aliases: Bool):
        self.implementation.set_templates_aliases(templates_aliases)

    @property 
    def templates_to_install(self) -> Bool:
        return self.implementation.templates_to_install 

    @emits_properties_changed
    def set_templates_to_install(self, templates_to_install: Bool):
        self.implementation.set_templates_to_install(templates_to_install)
        
    @property 
    def usbvm(self) -> Bool:
        return self.implementation.usbvm 

    @emits_properties_changed
    def set_usbvm(self, usbvm: Bool):
        self.implementation.set_usbvm(usbvm)
        
    @property 
    def usbvm_available(self) -> Bool:
        return self.implementation.usbvm_available 

    @emits_properties_changed
    def set_usbvm_available(self, usbvm_available: Bool):
        self.implementation.set_usbvm_available(usbvm_available)

    @property 
    def usbvm_with_netvm(self) -> Bool:
        return self.implementation.usbvm_with_netvm 

    @emits_properties_changed
    def set_usbvm_with_netvm(self, usbvm_with_netvm: Bool):
        self.implementation.set_usbvm_with_netvm(usbvm_with_netvm)

    @property 
    def vg_tpool(self) -> Bool:
        return self.implementation.vg_tpool 

    @emits_properties_changed
    def set_vg_tpool(self, vg_tpool: Bool):
        self.implementation.set_vg_tpool(vg_tpool)

    @property 
    def whonix_available(self) -> Bool:
        return self.implementation.whonix_available 

    @emits_properties_changed
    def set_whonix_available(self, whonix_available: Bool):
        self.implementation.set_whonix_available(whonix_available)
        
    @property 
    def whonix_default(self) -> Bool:
        return self.implementation.whonix_default 

    @emits_properties_changed
    def set_whonix_default(self, whonix_default: Bool):
        self.implementation.set_whonix_default(whonix_default)

    @property 
    def whonix_vms(self) -> Bool:
        return self.implementation.whonix_vms 

    @emits_properties_changed
    def set_whonix_vms(self, whonix_vms: Bool):
        self.implementation.set_whonix_vms(whonix_vms)

    @property
    def Reverse(self) -> Bool:
        """Whether to reverse order of lines in the hello world file."""
        return self.implementation.reverse

    @emits_properties_changed
    def SetReverse(self, reverse: Bool):
        self.implementation.set_reverse(reverse)

    @property
    def Lines(self) -> List[Str]:
        """Lines of the hello world file."""
        return self.implementation.lines

    @emits_properties_changed
    def SetLines(self, lines: List[Str]):
        self.implementation.set_lines(lines)
