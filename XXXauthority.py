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

__all__ = ["YYYAuthority"]


from taurus.core.taurusauthority import TaurusAuthority
from taurus import Factory

class YYYAuthority(TaurusAuthority):
    '''
    Dummy authority class for YYY 
    
    .. warning:: In most cases this class should not be instantiated directly.
                 Instead it should be done via :meth:`YYYFactory.getAuthority`
    '''

    # helper class property that stores a reference to the corresponding factory
    _factory = None
    _scheme = 'XXX'

    def __init__(self, session, parent=None, storeCallback=None):    
        self.call__init__(TaurusAuthority, session, parent)
