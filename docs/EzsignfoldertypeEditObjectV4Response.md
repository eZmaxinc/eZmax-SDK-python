# EzsignfoldertypeEditObjectV4Response

Response for PUT /4/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_edit_object_v4_response import EzsignfoldertypeEditObjectV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeEditObjectV4Response from a JSON string
ezsignfoldertype_edit_object_v4_response_instance = EzsignfoldertypeEditObjectV4Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeEditObjectV4Response.to_json())

# convert the object into a dict
ezsignfoldertype_edit_object_v4_response_dict = ezsignfoldertype_edit_object_v4_response_instance.to_dict()
# create an instance of EzsignfoldertypeEditObjectV4Response from a dict
ezsignfoldertype_edit_object_v4_response_from_dict = EzsignfoldertypeEditObjectV4Response.from_dict(ezsignfoldertype_edit_object_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


