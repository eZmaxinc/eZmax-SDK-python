"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_i_ezsignformfield_height import FieldIEzsignformfieldHeight
from eZmaxApi.model.field_i_ezsignformfield_width import FieldIEzsignformfieldWidth
from eZmaxApi.model.field_i_ezsignformfield_x import FieldIEzsignformfieldX
from eZmaxApi.model.field_i_ezsignformfield_y import FieldIEzsignformfieldY
from eZmaxApi.model.field_i_ezsignpage_pagenumber import FieldIEzsignpagePagenumber
from eZmaxApi.model.field_pki_ezsignformfield_id import FieldPkiEzsignformfieldID
globals()['FieldIEzsignformfieldHeight'] = FieldIEzsignformfieldHeight
globals()['FieldIEzsignformfieldWidth'] = FieldIEzsignformfieldWidth
globals()['FieldIEzsignformfieldX'] = FieldIEzsignformfieldX
globals()['FieldIEzsignformfieldY'] = FieldIEzsignformfieldY
globals()['FieldIEzsignpagePagenumber'] = FieldIEzsignpagePagenumber
globals()['FieldPkiEzsignformfieldID'] = FieldPkiEzsignformfieldID
from eZmaxApi.model.ezsignformfield_request import EzsignformfieldRequest


class TestEzsignformfieldRequest(unittest.TestCase):
    """EzsignformfieldRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignformfieldRequest(self):
        """Test EzsignformfieldRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignformfieldRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
