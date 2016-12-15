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

__all__ = ["YYYAttribute"]

from taurus.core.taurusattribute import TaurusAttribute
from taurus.core.taurusexception import TaurusException
from taurus.core.taurusbasetypes import DataType

class YYYAttribute(TaurusAttribute):
    '''
    A :class:`TaurusAttribute` that gives access to an YYY Process Variable.
    
    .. seealso:: :mod:`taurus.core.XXX` 
    
    .. warning:: In most cases this class should not be instantiated directly.
                 Instead it should be done via the :meth:`YYYFactory.getAttribute`
    '''

    # helper class property that stores a reference to the corresponding factory
    _factory = None
    _scheme = 'XXX'

    def __init__(self, name, parent, **kwargs):
        self.call__init__(TaurusAttribute, name, parent, **kwargs)
        # TODO

    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    # Necessary to overwrite
    #-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
    def isNumeric(self):
        return self.type in [DataType.Float, DataType.Integer]

    def isState(self):
		# TODO
        return False

    def encode(self, value):
		# TODO
        return value

    def decode(self, attr_value):
		# TODO
        return attr_value

    def write(self, value, with_read=True):
		# TODO
        raise TaurusException('Attributes are read-only')

    def read(self, cache=True):
		pass
		# TODO

    def poll(self):
		pass
		# TODO

    def _subscribeEvents(self):
		pass
		# TODO

    def _unsubscribeEvents(self):
		pass
		# TODO

    def isUsingEvents(self):
		pass
		# TODO
 
