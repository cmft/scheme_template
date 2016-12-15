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

__all__ = ["YYYAuthorityNameValidator", "YYYDeviceNameValidator", 
           "YYYAttributeNameValidator"]

from taurus import isValidName, debug
from taurus.core import TaurusElementType

from taurus.core.taurusvalidator import (TaurusAttributeNameValidator, 
                                         TaurusDeviceNameValidator, 
                                         TaurusAuthorityNameValidator)


class YYYAuthorityNameValidator(TaurusAuthorityNameValidator):
    # TODO Create your own grammatical expression. i.e    
    scheme = 'XXX'
    authority = 'TODO' #TODO e.g. //HOST:PORT
    path = '(?!)'
    query = '(?!)'
    fragment = '(?!)'


class YYYDeviceNameValidator(TaurusDeviceNameValidator): 
    # TODO Create your own grammatical expression. i.e    
    scheme = 'XXX'
    authority = YYYAuthorityNameValidator.authority
    path = 'TODO' #TODO e.g. r'(?P<devname>(\w+\.)+\w+))'
    query = '(?!)'
    fragment = '(?!)'

    def getNames(self, fullname, factory=None):
        """reimplemented from :class:`TaurusDeviceNameValidator`.
        """
        groups = self.getUriGroups(fullname)
        if groups is None:
            return None
        # TODO
        complete = 'Fullname: univocal name'
        normal = 'Normalname: univocal bane in a context'
        short = 'Shortname: Just a name'
        return complete, normal, short
 

class YYYAttributeNameValidator(TaurusAttributeNameValidator):        
    # TODO Create your own grammatical expression. i.e                 
    scheme = 'XXX'
    authority = YYYAuthorityNameValidator.authority
    path = 'TODO' #TODO e.g. ((r'(?!//)/?(%s/)?' + r'(?P<attrname>%s') % (YYYDeviceNameValidator.devname, attrname))
    query = '(?!)'
    fragment = '(?P<cfgkey>[^# ]*)'

    def getNames(self, fullname, factory=None, fragment=False):
        """reimplemented from :class:`TaurusAttributeNameValidator`.
        """
        groups = self.getUriGroups(fullname)
        if groups is None:
            return None
        #TODO
        # TODO
        complete = 'Fullname: univocal name'
        normal = 'Normalname: univocal bane in a context'
        short = 'Shortname: Just a name'

        if fragment:
            key = groups.get('fragment', None)
            return complete, normal, short, key

        return complete, normal, short
  
