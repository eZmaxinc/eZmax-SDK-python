# EzsignfolderReorderV2Response

Response for POST /2/object/ezsignfolder/{pkiEzsignfolderID}/reorder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_reorder_v2_response import EzsignfolderReorderV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderReorderV2Response from a JSON string
ezsignfolder_reorder_v2_response_instance = EzsignfolderReorderV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderReorderV2Response.to_json())

# convert the object into a dict
ezsignfolder_reorder_v2_response_dict = ezsignfolder_reorder_v2_response_instance.to_dict()
# create an instance of EzsignfolderReorderV2Response from a dict
ezsignfolder_reorder_v2_response_from_dict = EzsignfolderReorderV2Response.from_dict(ezsignfolder_reorder_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


