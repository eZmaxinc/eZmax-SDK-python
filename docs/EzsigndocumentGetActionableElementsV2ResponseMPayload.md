# EzsigndocumentGetActionableElementsV2ResponseMPayload

Payload for GET /2/object/ezsigndocument/{pkiEzsigndocumentID}/getActionableElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignsignature** | [**List[EzsignsignatureResponseCompound]**](EzsignsignatureResponseCompound.md) |  | 
**a_obj_ezsignformfieldgroup** | [**List[EzsignformfieldgroupResponseCompound]**](EzsignformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_actionable_elements_v2_response_m_payload import EzsigndocumentGetActionableElementsV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetActionableElementsV2ResponseMPayload from a JSON string
ezsigndocument_get_actionable_elements_v2_response_m_payload_instance = EzsigndocumentGetActionableElementsV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetActionableElementsV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_actionable_elements_v2_response_m_payload_dict = ezsigndocument_get_actionable_elements_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetActionableElementsV2ResponseMPayload from a dict
ezsigndocument_get_actionable_elements_v2_response_m_payload_from_dict = EzsigndocumentGetActionableElementsV2ResponseMPayload.from_dict(ezsigndocument_get_actionable_elements_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


