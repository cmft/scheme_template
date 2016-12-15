#!/usr/bin/env python

#############################################################################
##
# This file is part of Taurus
##
# http://taurus-scada.org
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Taurus is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Taurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
#############################################################################

"""Test for taurus.core.XXX.test.test_XXXvalidator..."""

__docformat__ = 'restructuredtext'


from taurus.external import unittest
from taurus.core.test import (valid, invalid, names,
                              AbstractNameValidatorTestCase)
from taurus.core.XXX.XXXvalidator import \
                                (YYYAuthorityNameValidator,
                                 YYYDeviceNameValidator,
                                 YYYAttributeNameValidator)
from taurus import tauruscustomsettings


#=========================================================================
# Tests for YYY Authority name validation
#=========================================================================
@valid(name='XXX://....') # TODO replace the .... for the corresponding URI
@invalid(name='XXX:....')
@names(name='XXX://....',
       out=('XXX://...', '//....', '....'))
class YYYAuthValidatorTestCase(AbstractNameValidatorTestCase,
                                 unittest.TestCase):
    validator = YYYAuthorityNameValidator

#=========================================================================
# Tests for YYY Device name validation
#=========================================================================
@valid(name='XXX://....') # TODO replace the .... for the corresponding URI
@invalid(name='XXX:/....')
@names(name='XXX://....',
       out=('XXX://...', '....', '....'))
class YYYDevValidatorTestCase(AbstractNameValidatorTestCase,
                                 unittest.TestCase):
    validator = YYYDeviceNameValidator

#=========================================================================
# Tests for YYY Attribute name validation
#=========================================================================
@valid(name='XXX://....') # TODO replace the .... for the corresponding URI
@invalid(name='XXX:/....')
@names(name='XXX://....',
       out=('XXX://...', '....', '....'))
class XXXAttrValidatorTestCase(AbstractNameValidatorTestCase,
                                 unittest.TestCase):
    validator = YYYAttributeNameValidator

