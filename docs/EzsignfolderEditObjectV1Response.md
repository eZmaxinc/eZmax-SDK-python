# EzsignfolderEditObjectV1Response

Response for PUT /1/object/ezsignfolder/{pkiEzsignfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_edit_object_v1_response import EzsignfolderEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderEditObjectV1Response from a JSON string
ezsignfolder_edit_object_v1_response_instance = EzsignfolderEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignfolderEditObjectV1Response.to_json()

# convert the object into a dict
ezsignfolder_edit_object_v1_response_dict = ezsignfolder_edit_object_v1_response_instance.to_dict()
# create an instance of EzsignfolderEditObjectV1Response from a dict
ezsignfolder_edit_object_v1_response_form_dict = ezsignfolder_edit_object_v1_response.from_dict(ezsignfolder_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


