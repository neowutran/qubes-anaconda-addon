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

from pyanaconda.core.configuration.anaconda import conf
from pyanaconda.core.dbus import DBus
from pyanaconda.core.signal import Signal
from pyanaconda.modules.common.base import KickstartService
from pyanaconda.modules.common.containers import TaskContainer

from org_qubes_initial_setup.constants import INITIAL_SETUP
from org_qubes_initial_setup.service.initial_setup_interface import InitialSetupInterface
from org_qubes_initial_setup.service.kickstart import InitialSetupKickstartSpecification

log = logging.getLogger(__name__)


class InitialSetup(KickstartService):
    """The InitialSetup D-Bus service.

    This class parses and stores data for the Initial Setup addon.
    """

    def __init__(self):
        super().__init__()
        self._allow_usb_mouse = False
        self._bool_options = False
        self._custom_pool = False
        self._debian_available = False
        self._default_template = False
        self._default_vms = False
        self._disp_firewallvm_and_usbvm = False
        self._disp_netvm = False
        self._fedora_available = False
        self._gui_mode = False
        self._seen = False
        self._skip = False
        self._system_vms = False
        self._templates_aliases = False
        self._templates_to_install = False
        self._usbvm = False
        self._usbvm_available = False
        self._usbvm_with_netvm = False
        self._vg_tpool = False
        self._whonix_available = False
        self._whonix_default = False
        self._whonix_vms = False

        self.allow_usb_mouse_changed = Signal()
        self.bool_options_changed = Signal()
        self.custom_pool_changed = Signal()
        self.debian_available_changed = Signal()
        self.default_template_changed = Signal()
        self.default_vms_changed = Signal()
        self.disp_firewallvm_and_usbvm_changed = Signal()
        self.disp_netvm_changed = Signal()
        self.fedora_available_changed = Signal()
        self.gui_mode_changed = Signal()
        self.seen_changed = Signal()
        self.skip_changed = Signal()
        self.system_vms_changed = Signal()
        self.templates_aliases_changed = Signal()
        self.templates_to_install_changed = Signal()
        self.usbvm_changed = Signal()
        self.usbvm_available_changed = Signal()
        self.usbvm_with_netvm_changed = Signal()
        self.vg_tpool_changed = Signal()
        self.whonix_available_changed = Signal()
        self.whonix_default_changed = Signal()
        self.whonix_vms_changed = Signal()

    def publish(self):
        """Publish the module."""
        TaskContainer.set_namespace(INITIAL_SETUP.namespace)
        DBus.publish_object(INITIAL_SETUP.object_path, InitialSetupInterface(self))
        DBus.register_service(INITIAL_SETUP.service_name)

    @property
    def kickstart_specification(self):
        """Return the kickstart specification."""
        return InitialSetupKickstartSpecification

    def process_kickstart(self, data):
        """Process the kickstart data."""
        log.debug("Processing kickstart data...")
        self._allow_usb_mouse = data.addons.org_qubes_initial_setup.allow_usb_mouse
        self._bool_options = data.addons.org_qubes_initial_setup.bool_options
        self._custom_pool = data.addons.org_qubes_initial_setup.custom_pool
        self._debian_available = data.addons.org_qubes_initial_setup.debian_available
        self._default_template = data.addons.org_qubes_initial_setup.default_template
        self._default_vms = data.addons.org_qubes_initial_setup.default_vms
        self._disp_firewallvm_and_usbvm = data.addons.org_qubes_initial_setup.disp_firewallvm_and_usbvm
        self._disp_netvm = data.addons.org_qubes_initial_setup.disp_netvm
        self._fedora_available = data.addons.org_qubes_initial_setup.fedora_available
        self._gui_mode = data.addons.org_qubes_initial_setup.gui_mode
        self._seen = data.addons.org_qubes_initial_setup.seen
        self._skip = data.addons.org_qubes_initial_setup.skip
        self._system_vms = data.addons.org_qubes_initial_setup.system_vms
        self._templates_aliases = data.addons.org_qubes_initial_setup.templates_aliases
        self._templates_to_install = data.addons.org_qubes_initial_setup.templates_to_install
        self._usbvm = data.addons.org_qubes_initial_setup.usbvm
        self._usbvm_available = data.addons.org_qubes_initial_setup.usbvm_available
        self._usbvm_with_netvm = data.addons.org_qubes_initial_setup.usbvm_with_netvm
        self._vg_tpool = data.addons.org_qubes_initial_setup.vg_tpool
        self._whonix_available = data.addons.org_qubes_initial_setup.whonix_available
        self._whonix_default = data.addons.org_qubes_initial_setup.whonix_default
        self._whonix_vms = data.addons.org_qubes_initial_setup.whonix_vms

    def setup_kickstart(self, data):
        """Set the given kickstart data."""
        log.debug("Generating kickstart data...")
        data.addons.org_qubes_initial_setup.allow_usb_mouse = self._allow_usb_mouse
        data.addons.org_qubes_initial_setup.bool_options = self._bool_options
        data.addons.org_qubes_initial_setup.custom_pool = self._custom_pool
        data.addons.org_qubes_initial_setup.debian_available = self._debian_available
        data.addons.org_qubes_initial_setup.default_template = self._default_template
        data.addons.org_qubes_initial_setup.default_vms = self._default_vms
        data.addons.org_qubes_initial_setup.disp_firewallvm_and_usbvm = self._disp_firewallvm_and_usbvm
        data.addons.org_qubes_initial_setup.disp_netvm = self._disp_netvm
        data.addons.org_qubes_initial_setup.fedora_available = self._fedora_available
        data.addons.org_qubes_initial_setup.gui_mode = self._gui_mode
        data.addons.org_qubes_initial_setup.seen = self._seen
        data.addons.org_qubes_initial_setup.skip = self._skip
        data.addons.org_qubes_initial_setup.system_vms = self._system_vms
        data.addons.org_qubes_initial_setup.templates_aliases = self._templates_aliases
        data.addons.org_qubes_initial_setup.templates_to_install = self._templates_to_install
        data.addons.org_qubes_initial_setup.usbvm = self._usbvm
        data.addons.org_qubes_initial_setup.usbvm_available = self._usbvm_available
        data.addons.org_qubes_initial_setup.usbvm_with_netvm = self._usbvm_with_netvm
        data.addons.org_qubes_initial_setup.vg_tpool = self._vg_tpool
        data.addons.org_qubes_initial_setup.whonix_available = self._whonix_available
        data.addons.org_qubes_initial_setup.whonix_default = self._whonix_default
        data.addons.org_qubes_initial_setup.whonix_vms = self._whonix_vms

    @property
    def allow_usb_mouse(self):
        return self._allow_usb_mouse

    def set_allow_usb_mouse(self, allow_usb_mouse):
        self._allow_usb_mouse = allow_usb_mouse
        self.reverse_changed.emit()
        log.debug("allow_usb_mouse is set to %s.", allow_usb_mouse)

    @property
    def bool_options(self):
        return self._bool_options

    def set_bool_options(self, bool_options):
        self._bool_options = bool_options
        self.reverse_changed.emit()
        log.debug("bool_options is set to %s.", bool_options)

    @property
    def custom_pool(self):
        return self._custom_pool

    def set_custom_pool(self, custom_pool):
        self._custom_pool = custom_pool
        self.reverse_changed.emit()
        log.debug("custom_pool is set to %s.", custom_pool)

    @property
    def debian_available(self):
        return self._debian_available

    def set_debian_available(self, debian_available):
        self._debian_available = debian_available
        self.reverse_changed.emit()
        log.debug("debian_available is set to %s.", debian_available)

    @property
    def default_template(self):
        return self._default_template

    def set_default_template(self, default_template):
        self._default_template = default_template
        self.reverse_changed.emit()
        log.debug("default_template is set to %s.", default_template)

    @property
    def default_vms(self):
        return self._default_vms

    def set_default_vms(self, default_vms):
        self._default_vms = default_vms
        self.reverse_changed.emit()
        log.debug("default_vms is set to %s.", default_vms)

    @property
    def disp_firewallvm_and_usbvm(self):
        return self._disp_firewallvm_and_usbvm

    def set_disp_firewallvm_and_usbvm(self, disp_firewallvm_and_usbvm):
        self._disp_firewallvm_and_usbvm = disp_firewallvm_and_usbvm
        self.reverse_changed.emit()
        log.debug("disp_firewallvm_and_usbvm is set to %s.", disp_firewallvm_and_usbvm)

    @property
    def disp_netvm(self):
        return self._disp_netvm

    def set_disp_netvm(self, disp_netvm):
        self._disp_netvm = disp_netvm
        self.reverse_changed.emit()
        log.debug("disp_netvm is set to %s.", disp_netvm)

    @property
    def fedora_available(self):
        return self._fedora_available

    def set_fedora_available(self, fedora_available):
        self._fedora_available = fedora_available
        self.reverse_changed.emit()
        log.debug("fedora_available is set to %s.", fedora_available)

    @property
    def gui_mode(self):
        return self._gui_mode

    def set_gui_mode(self, gui_mode):
        self._gui_mode = gui_mode
        self.reverse_changed.emit()
        log.debug("gui_mode is set to %s.", gui_mode)

    @property
    def seen(self):
        return self._seen

    def set_seen(self, seen):
        self._seen = seen
        self.reverse_changed.emit()
        log.debug("seen is set to %s.", seen)

    @property
    def skip(self):
        return self._skip

    def set_skip(self, skip):
        self._skip = skip
        self.reverse_changed.emit()
        log.debug("skip is set to %s.", skip)

    @property
    def system_vms(self):
        return self._system_vms

    def set_system_vms(self, system_vms):
        self._system_vms = system_vms
        self.reverse_changed.emit()
        log.debug("system_vms is set to %s.", system_vms)

    @property
    def templates_aliases(self):
        return self._templates_aliases

    def set_templates_aliases(self, templates_aliases):
        self._templates_aliases = templates_aliases
        self.reverse_changed.emit()
        log.debug("templates_aliases is set to %s.", templates_aliases)

    @property
    def templates_to_install(self):
        return self._templates_to_install

    def set_templates_to_install(self, templates_to_install):
        self._templates_to_install = templates_to_install
        self.reverse_changed.emit()
        log.debug("templates_to_install is set to %s.", templates_to_install)

    @property
    def usbvm(self):
        return self._usbvm

    def set_usbvm(self, usbvm):
        self._usbvm = usbvm
        self.reverse_changed.emit()
        log.debug("usbvm is set to %s.", usbvm)

    @property
    def usbvm_available(self):
        return self._usbvm_available

    def set_usbvm_available(self, usbvm_available):
        self._usbvm_available = usbvm_available
        self.reverse_changed.emit()
        log.debug("usbvm_available is set to %s.", usbvm_available)

    @property
    def usbvm_with_netvm(self):
        return self._usbvm_with_netvm

    def set_usbvm_with_netvm(self, usbvm_with_netvm):
        self._usbvm_with_netvm = usbvm_with_netvm
        self.reverse_changed.emit()
        log.debug("usbvm_with_netvm is set to %s.", usbvm_with_netvm)

    @property
    def vg_tpool(self):
        return self._vg_tpool

    def set_vg_tpool(self, vg_tpool):
        self._vg_tpool = vg_tpool
        self.reverse_changed.emit()
        log.debug("vg_tpool is set to %s.", vg_tpool)

    @property
    def whonix_available(self):
        return self._whonix_available

    def set_whonix_available(self, whonix_available):
        self._whonix_available = whonix_available
        self.reverse_changed.emit()
        log.debug("whonix_available is set to %s.", whonix_available)

    @property
    def whonix_default(self):
        return self._whonix_default

    def set_whonix_default(self, whonix_default):
        self._whonix_default = whonix_default
        self.reverse_changed.emit()
        log.debug("whonix_default is set to %s.", whonix_default)

    @property
    def whonix_vms(self):
        return self._whonix_vms

    def set_whonix_vms(self, whonix_vms):
        self._whonix_vms = whonix_vms
        self.reverse_changed.emit()
        log.debug("whonix_vms is set to %s.", whonix_vms)

    @property
    def reverse(self):
        """Whether to reverse order of lines in the hello world file."""
        return self._reverse

    def set_reverse(self, reverse):
        self._reverse = reverse
        self.reverse_changed.emit()
        log.debug("Reverse is set to %s.", reverse)

    @property
    def lines(self):
        """Lines of the hello world file."""
        return self._lines

    def set_lines(self, lines):
        self._lines = lines
        self.lines_changed.emit()
        log.debug("Lines is set to %s.", lines)

    def configure_with_tasks(self):
        """Return configuration tasks.

        The configuration tasks are run at the beginning of the installation process.

        Anaconda's code automatically calls the ***_with_tasks methods and
        stores the returned ***Task instances to later execute their run() methods.
        """
        return []

    def install_with_tasks(self):
        """Return installation tasks.

        The installation tasks are run at the end of the installation process.

        Anaconda's code automatically calls the ***_with_tasks methods and
        stores the returned ***Task instances to later execute their run() methods.
        """
        return []
