# EzsignfolderGetActionableElementsV3Response

Response for GET /3/object/ezsignfolder/{pkiEzsignfolderID}/getActionableElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderGetActionableElementsV3ResponseMPayload**](EzsignfolderGetActionableElementsV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_actionable_elements_v3_response import EzsignfolderGetActionableElementsV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetActionableElementsV3Response from a JSON string
ezsignfolder_get_actionable_elements_v3_response_instance = EzsignfolderGetActionableElementsV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetActionableElementsV3Response.to_json())

# convert the object into a dict
ezsignfolder_get_actionable_elements_v3_response_dict = ezsignfolder_get_actionable_elements_v3_response_instance.to_dict()
# create an instance of EzsignfolderGetActionableElementsV3Response from a dict
ezsignfolder_get_actionable_elements_v3_response_from_dict = EzsignfolderGetActionableElementsV3Response.from_dict(ezsignfolder_get_actionable_elements_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


