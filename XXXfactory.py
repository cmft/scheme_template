#!/usr/bin/env python
#############################################################################
##
## This file is part of Taurus
## 
## http://taurus-scada.org
##
## Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
## 
## Taurus is free software: you can redistribute it and/or modify
## it under the terms of the GNU Lesser General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Taurus is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public License
## along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

__all__ = ['YYYFactory']


import weakref

from taurus.core.taurusbasetypes import TaurusElementType
from XXXattribute import YYYAttribute
from XXXauthority import YYYAuthority
from XXXdevice import YYYDevice
from taurus.core.taurusexception import TaurusException
from taurus.core.util.log import Logger
from taurus.core.util.singleton import Singleton
from taurus.core.taurusfactory import TaurusFactory

class YYYFactory(Singleton, TaurusFactory, Logger):
    """
    A Singleton class that provides YYY related objects.
    """
    schemes = ("XXX",)
    elementTypesMap = {TaurusElementType.Authority: YYYAuthority,
                       TaurusElementType.Device: YYYDevice,
                       TaurusElementType.Attribute: YYYAttribute
                       }

    def __init__(self):
        """ Initialization. Nothing to be done here for now."""
        pass

    def init(self, *args, **kwargs):
        """Singleton instance initialization."""
        name = self.__class__.__name__
        self.call__init__(Logger, name)
        self.call__init__(TaurusFactory)
        # TODO
        self._attrs = weakref.WeakValueDictionary()
        self._devs = weakref.WeakValueDictionary()
        self._auth = None
        self.scheme = "XXX"

    def getAuthority(self, auth_name=None):
        """Obtain the YYYDatabase object.
        :return: (YYYAuthority)
        """
		# TODO
        pass

    def getDevice(self, dev_name):
        """Obtain the object corresponding to the given device name. If the 
        corresponding device already exists, the existing instance is returned. 
        Otherwise a new instance is stored and returned.
           
        :param dev_name: (str) the device name string. See
                         :mod:`taurus.core.XXX` for valid device names
        
        :return: (YYYDevice)
         
        @throws TaurusException if the given name is invalid.
        """
        # TODO
        v = self.getDeviceNameValidator()
        if not v.isValid(dev_name):
            raise TaurusException("Invalid YYY device name %s" % dev_name)

        fullname, _, _ = v.getNames(dev_name)
        dev = self._devs.get(fullname)
        if dev is not None:
            return dev

        dev = YYYDevice(fullname)
        return dev
        
    def getAttribute(self, attr_name):
        """Obtain the object corresponding to the given attribute name. If the 
        corresponding attribute already exists, the existing instance is
        returned. Otherwise a new instance is stored and returned. The evaluator
        device associated to this attribute will also be created if necessary.
           
        :param attr_name: (str) the attribute name string. See
                          :mod:`taurus.core.XXX` for valid attribute 
                          names
        
        :return: (YYYAttribute)
         
        @throws TaurusException if the given name is invalid.
        """
		# TODO
        v = self.getAttributeNameValidator()
        fullname, _, _ = v.getNames(attr_name)
        if not v.isValid(attr_name):
            raise TaurusException("Invalid YYY attribute name %s" % attr_name)

        attr = self._attrs.get(fullname)
        if attr is not None:
            return attr

        devname = v.getUriGroups(fullname).get('devname')
        dev = self._devs.get(fullname)
        if dev is not None:
            dev = self.getDevice(devname)
        attr = YYYAttribute(fullname, dev)
        return attr

    def addAttributeToPolling(self, attribute, period, unsubscribe_evts=False):
        """Activates the polling (client side) for the given attribute with the
           given period (seconds).

           :param attribute: (taurus.core.tango.TangoAttribute) attribute name.
           :param period: (float) polling period (in seconds)
           :param unsubscribe_evts: (bool) whether or not to unsubscribe from events
        """
        pass
		# TODO

    def removeAttributeFromPolling(self, attribute):
        """Deactivate the polling (client side) for the given attribute. If the
           polling of the attribute was not previously enabled, nothing happens.

           :param attribute: (str) attribute name.
        """
        pass
		# TODO

    def getAuthorityNameValidator(self):
        """Return YYYDatabaseNameValidator"""
        import XXXvalidator
        return XXXvalidator.YYYAuthorityNameValidator()
                 
    def getDeviceNameValidator(self):
        """Return YYYDeviceNameValidator"""
        import XXXvalidator
        return XXXvalidator.YYYDeviceNameValidator()

    def getAttributeNameValidator(self):
        """Return YYYAttributeNameValidator"""
        import XXXvalidator
        return XXXvalidator.YYYAttributeNameValidator()
