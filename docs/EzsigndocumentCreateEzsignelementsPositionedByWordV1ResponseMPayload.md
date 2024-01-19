# EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload

Payload for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/createEzsignelementsPositionedByWord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsignsignature_id** | **List[int]** |  | 
**a_pki_ezsignformfieldgroup_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload import EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload from a JSON string
ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload_instance = EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload_dict = ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV1ResponseMPayload from a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload_form_dict = ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload.from_dict(ezsigndocument_create_ezsignelements_positioned_by_word_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


