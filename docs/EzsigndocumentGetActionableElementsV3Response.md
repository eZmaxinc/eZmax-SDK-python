# EzsigndocumentGetActionableElementsV3Response

Response for GET /3/object/ezsigndocument/{pkiEzsigndocumentID}/getActionableElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentGetActionableElementsV3ResponseMPayload**](EzsigndocumentGetActionableElementsV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_actionable_elements_v3_response import EzsigndocumentGetActionableElementsV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetActionableElementsV3Response from a JSON string
ezsigndocument_get_actionable_elements_v3_response_instance = EzsigndocumentGetActionableElementsV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetActionableElementsV3Response.to_json())

# convert the object into a dict
ezsigndocument_get_actionable_elements_v3_response_dict = ezsigndocument_get_actionable_elements_v3_response_instance.to_dict()
# create an instance of EzsigndocumentGetActionableElementsV3Response from a dict
ezsigndocument_get_actionable_elements_v3_response_from_dict = EzsigndocumentGetActionableElementsV3Response.from_dict(ezsigndocument_get_actionable_elements_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


