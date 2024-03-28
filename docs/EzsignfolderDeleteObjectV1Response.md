# EzsignfolderDeleteObjectV1Response

Response for DELETE /1/object/ezsignfolder/{pkiEzsignfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_delete_object_v1_response import EzsignfolderDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderDeleteObjectV1Response from a JSON string
ezsignfolder_delete_object_v1_response_instance = EzsignfolderDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsignfolder_delete_object_v1_response_dict = ezsignfolder_delete_object_v1_response_instance.to_dict()
# create an instance of EzsignfolderDeleteObjectV1Response from a dict
ezsignfolder_delete_object_v1_response_form_dict = ezsignfolder_delete_object_v1_response.from_dict(ezsignfolder_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


