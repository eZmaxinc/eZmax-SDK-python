# EzsigndocumentGetCompletedElementsV1ResponseMPayload

Payload for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}/getCompletedElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureResponseCompound]**](EzsignsignatureResponseCompound.md) |  | 
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupResponseCompound]**](EzsignformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_completed_elements_v1_response_m_payload import EzsigndocumentGetCompletedElementsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetCompletedElementsV1ResponseMPayload from a JSON string
ezsigndocument_get_completed_elements_v1_response_m_payload_instance = EzsigndocumentGetCompletedElementsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetCompletedElementsV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_completed_elements_v1_response_m_payload_dict = ezsigndocument_get_completed_elements_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetCompletedElementsV1ResponseMPayload from a dict
ezsigndocument_get_completed_elements_v1_response_m_payload_from_dict = EzsigndocumentGetCompletedElementsV1ResponseMPayload.from_dict(ezsigndocument_get_completed_elements_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


