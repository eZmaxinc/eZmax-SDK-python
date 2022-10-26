"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import eZmaxApi
from eZmaxApi.model.field_i_ezsignpage_heightimage import FieldIEzsignpageHeightimage
from eZmaxApi.model.field_i_ezsignpage_heightpdf import FieldIEzsignpageHeightpdf
from eZmaxApi.model.field_i_ezsignpage_pagenumber import FieldIEzsignpagePagenumber
from eZmaxApi.model.field_i_ezsignpage_widthimage import FieldIEzsignpageWidthimage
from eZmaxApi.model.field_i_ezsignpage_widthpdf import FieldIEzsignpageWidthpdf
from eZmaxApi.model.field_pki_ezsignpage_id import FieldPkiEzsignpageID
globals()['FieldIEzsignpageHeightimage'] = FieldIEzsignpageHeightimage
globals()['FieldIEzsignpageHeightpdf'] = FieldIEzsignpageHeightpdf
globals()['FieldIEzsignpagePagenumber'] = FieldIEzsignpagePagenumber
globals()['FieldIEzsignpageWidthimage'] = FieldIEzsignpageWidthimage
globals()['FieldIEzsignpageWidthpdf'] = FieldIEzsignpageWidthpdf
globals()['FieldPkiEzsignpageID'] = FieldPkiEzsignpageID
from eZmaxApi.model.ezsignpage_response import EzsignpageResponse


class TestEzsignpageResponse(unittest.TestCase):
    """EzsignpageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEzsignpageResponse(self):
        """Test EzsignpageResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EzsignpageResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
