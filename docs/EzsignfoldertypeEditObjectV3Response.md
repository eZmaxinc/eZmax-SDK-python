# EzsignfoldertypeEditObjectV3Response

Response for PUT /3/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_edit_object_v3_response import EzsignfoldertypeEditObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeEditObjectV3Response from a JSON string
ezsignfoldertype_edit_object_v3_response_instance = EzsignfoldertypeEditObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeEditObjectV3Response.to_json())

# convert the object into a dict
ezsignfoldertype_edit_object_v3_response_dict = ezsignfoldertype_edit_object_v3_response_instance.to_dict()
# create an instance of EzsignfoldertypeEditObjectV3Response from a dict
ezsignfoldertype_edit_object_v3_response_from_dict = EzsignfoldertypeEditObjectV3Response.from_dict(ezsignfoldertype_edit_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


