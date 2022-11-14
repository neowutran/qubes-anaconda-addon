#
# Copyright (C) 2013  Red Hat, Inc.
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
# Red Hat Author(s): Vratislav Podzimek <vpodzime@redhat.com>
#
#
# NOTE: Anaconda is using Simpleline library for Text User Interface.
#       To learn how to use Simpleline look on the documentation:
#
#       http://python-simpleline.readthedocs.io/en/latest/
#


"""Module with the class for the Hello world TUI spoke."""

import logging
import re

from simpleline.render.prompt import Prompt
from simpleline.render.screen import InputState
from simpleline.render.containers import ListColumnContainer
from simpleline.render.widgets import CheckboxWidget, EntryWidget

from pyanaconda.core.constants import PASSWORD_POLICY_ROOT
from pyanaconda.ui.tui.spokes import NormalTUISpoke
from pyanaconda.ui.common import FirstbootSpokeMixIn
# Simpleline's dialog configured for use in Anaconda
from pyanaconda.ui.tui.tuiobject import Dialog, PasswordDialog

# the path to addons is in sys.path so we can import things from org_fedora_hello_world
from org_qubes_initial_setup.categories.hello_world import InitialSetupCategory
from org_qubes_initial_setup.constants import INITIAL_SETUP

log = logging.getLogger(__name__)

# export only the HelloWorldSpoke and HelloWorldEditSpoke classes
__all__ = ["QubesOsSpoke"]

# import gettext
# _ = lambda x: gettext.ldgettext("hello-world-anaconda-plugin", x)

# will never be translated
_ = lambda x: x
N_ = lambda x: x


class QubesOsSpoke(FirstbootSpokeMixIn, NormalTUISpoke):
    """
    Class for the Hello world TUI spoke that is a subclass of NormalTUISpoke. It
    is a simple example of the basic unit for Anaconda's text user interface.
    Since it is also inherited form the FirstbootSpokeMixIn, it will also appear
    in the Initial Setup (successor of the Firstboot tool).

    :see: pyanaconda.ui.tui.TUISpoke
    :see: pyanaconda.ui.common.FirstbootSpokeMixIn
    :see: simpleline.render.widgets.Widget
    """

    ### class attributes defined by API ###

    # category this spoke belongs to
    category = InitialSetupCategory

    def __init__(self, *args, **kwargs):
        """
        Create the representation of the spoke.

        :see: simpleline.render.screen.UIScreen
        """
        super().__init__(*args, **kwargs)
        self.title = N_("Qubes OS")
        self._initial_setup_module = INITIAL_SETUP.get_proxy()
        self._container = None
        self.qubes_data = self._initial_setup_module

        self.initialize_done()

    def initialize(self):
        """
        The initialize method that is called after the instance is created.
        The difference between __init__ and this method is that this may take
        a long time and thus could be called in a separated thread.

        :see: pyanaconda.ui.common.UIObject.initialize
        """
        super().initialize()

    def setup(self, args=None):
        """
        The setup method that is called right before the spoke is entered.
        It should update its state according to the contents of DBus modules.

        :see: simpleline.render.screen.UIScreen.setup
        """
        super().setup(args)

        for attr in self.qubes_data.bool_options:
            setattr(self, '_' + attr, getattr(self.qubes_data, attr))

        return True

    def _add_checkbox(self, name, title):
        w = CheckboxWidget(title=title, completed=getattr(self, name))
        self._container.add(w, self._set_checkbox, name)

    def refresh(self, args=None):
        """
        The refresh method that is called every time the spoke is displayed.
        It should generate the UI elements according to its state.

        :see: pyanaconda.ui.common.UIObject.refresh
        :see: simpleline.render.screen.UIScreen.refresh
        :param args: optional argument that may be used when the screen is
                     scheduled
        :type args: anything
        """
        # call parent method to setup basic container with screen title set
        super().refresh(args)

        self._container = ListColumnContainer(
            columns=1
        )
        w = CheckboxWidget(title=_('Create default system qubes '
                                   '(sys-net, sys-firewall, default DispVM)'),
                           completed=self._system_vms)
        self._container.add(w, self._set_checkbox, '_system_vms')
        if self._system_vms:
            w = CheckboxWidget(
                title=_('Make sys-firewall and sys-usb disposable'),
                completed=self._disp_firewallvm_and_usbvm)
            self._container.add(
                w,
                self._set_checkbox,
                '_disp_firewallvm_and_usbvm')
            w = CheckboxWidget(
                title=_('Make sys-net disposable'),
                completed=self._disp_netvm)
            self._container.add(w, self._set_checkbox, '_disp_netvm')
        w = CheckboxWidget(title=_('Create default application qubes '
                                   '(personal, work, untrusted, vault)'),
                           completed=self._default_vms)
        self._container.add(w, self._set_checkbox, '_default_vms')
        if self.qubes_data.whonix_available:
            w = CheckboxWidget(
                title=_('Create Whonix Gateway and Workstation qubes '
                        '(sys-whonix, anon-whonix)'),
                completed=self._whonix_vms)
            self._container.add(w, self._set_checkbox, '_whonix_vms')
        if self._whonix_vms:
            w = CheckboxWidget(
                title=_('Enable system and template updates over the Tor anonymity '
                        'network using Whonix'),
                completed=self._whonix_default)
            self._container.add(w, self._set_checkbox, '_whonix_default')
        if self.qubes_data.usbvm_available:
            w = CheckboxWidget(
                title=_('Create USB qube holding all USB controllers (sys-usb)'),
                completed=self._usbvm)
            self._container.add(w, self._set_checkbox, '_usbvm')
        if self._usbvm:
            w = CheckboxWidget(
                title=_('Use sys-net qube for both networking and USB devices'),
                completed=self._usbvm_with_netvm)
            self._container.add(w, self._set_checkbox, '_usbvm_with_netvm')
        if self._usbvm:
            w = CheckboxWidget(
                title=_('Automatically accept USB mice (discouraged)'),
                completed=self._allow_usb_mouse)
            self._container.add(w, self._set_checkbox, '_allow_usb_mouse')

        self.window.add_with_separator(self._container)

    def _set_checkbox(self, name):
        setattr(self, name, not getattr(self, name))

    def apply(self):
        """
        The apply method that is called when the spoke is left. It should
        update the contents of self.data with values set in the spoke.

        """

        for attr in self.qubes_data.bool_options:
            setattr(self.qubes_data, attr, getattr(self, '_' + attr))

        self.qubes_data.seen = True

    def execute(self):
        """
        The execute method is not called automatically for TUI. It should be called
        in input() if required. It is supposed to do all changes to the runtime
        environment according to the values set in the spoke.
        """
        # nothing to do here
        pass

    @property
    def completed(self):
        """
        The completed property that tells whether all mandatory items on the
        spoke are set, or not. The spoke will be marked on the hub as completed
        or uncompleted according to the returned value.

        :rtype: bool
        """
        return self.qubes_data.seen

    @property
    def status(self):
        """
        The status property that is a brief string describing the state of the
        spoke. It should describe whether all values are set and if possible
        also the values themselves. The returned value will appear on the hub
        below the spoke's title.

        :rtype: str
        """
        return ""

    def input(self, args, key):
        """
        The input method that is called by the main loop on user's input.

        :param args: optional argument that may be used when the screen is
                     scheduled
        :type args: anything
        :param key: user's input
        :type key: unicode
        :return: if the input should not be handled here, return it, otherwise
                 return InputState.PROCESSED or InputState.DISCARDED if the input was
                 processed successfully or not respectively
        :rtype: enum InputState
        """
        if self._container.process_user_input(key):
            self.apply()
            return InputState.PROCESSED_AND_REDRAW

        return super().input(args, key)
