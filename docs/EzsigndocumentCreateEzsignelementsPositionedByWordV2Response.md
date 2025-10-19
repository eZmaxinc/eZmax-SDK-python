# EzsigndocumentCreateEzsignelementsPositionedByWordV2Response

Response for POST /2/object/ezsigndocument/{pkiEzsigndocumentID}/createEzsignelementsPositionedByWord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentCreateEzsignelementsPositionedByWordV2ResponseMPayload**](EzsigndocumentCreateEzsignelementsPositionedByWordV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_create_ezsignelements_positioned_by_word_v2_response import EzsigndocumentCreateEzsignelementsPositionedByWordV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV2Response from a JSON string
ezsigndocument_create_ezsignelements_positioned_by_word_v2_response_instance = EzsigndocumentCreateEzsignelementsPositionedByWordV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentCreateEzsignelementsPositionedByWordV2Response.to_json())

# convert the object into a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v2_response_dict = ezsigndocument_create_ezsignelements_positioned_by_word_v2_response_instance.to_dict()
# create an instance of EzsigndocumentCreateEzsignelementsPositionedByWordV2Response from a dict
ezsigndocument_create_ezsignelements_positioned_by_word_v2_response_from_dict = EzsigndocumentCreateEzsignelementsPositionedByWordV2Response.from_dict(ezsigndocument_create_ezsignelements_positioned_by_word_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


