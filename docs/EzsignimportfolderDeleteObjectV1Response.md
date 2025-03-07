# EzsignimportfolderDeleteObjectV1Response

Response for DELETE /1/object/ezsignimportfolder/{pkiEzsignimportfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignimportfolder_delete_object_v1_response import EzsignimportfolderDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportfolderDeleteObjectV1Response from a JSON string
ezsignimportfolder_delete_object_v1_response_instance = EzsignimportfolderDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignimportfolderDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsignimportfolder_delete_object_v1_response_dict = ezsignimportfolder_delete_object_v1_response_instance.to_dict()
# create an instance of EzsignimportfolderDeleteObjectV1Response from a dict
ezsignimportfolder_delete_object_v1_response_from_dict = EzsignimportfolderDeleteObjectV1Response.from_dict(ezsignimportfolder_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


