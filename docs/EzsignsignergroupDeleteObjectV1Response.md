# EzsignsignergroupDeleteObjectV1Response

Response for DELETE /1/object/ezsignsignergroup/{pkiEzsignsignergroupID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_delete_object_v1_response import EzsignsignergroupDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupDeleteObjectV1Response from a JSON string
ezsignsignergroup_delete_object_v1_response_instance = EzsignsignergroupDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsignsignergroup_delete_object_v1_response_dict = ezsignsignergroup_delete_object_v1_response_instance.to_dict()
# create an instance of EzsignsignergroupDeleteObjectV1Response from a dict
ezsignsignergroup_delete_object_v1_response_from_dict = EzsignsignergroupDeleteObjectV1Response.from_dict(ezsignsignergroup_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


