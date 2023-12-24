# EzsignsignergroupCreateObjectV1Response

Response for POST /1/object/ezsignsignergroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignergroupCreateObjectV1ResponseMPayload**](EzsignsignergroupCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_create_object_v1_response import EzsignsignergroupCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupCreateObjectV1Response from a JSON string
ezsignsignergroup_create_object_v1_response_instance = EzsignsignergroupCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupCreateObjectV1Response.to_json()

# convert the object into a dict
ezsignsignergroup_create_object_v1_response_dict = ezsignsignergroup_create_object_v1_response_instance.to_dict()
# create an instance of EzsignsignergroupCreateObjectV1Response from a dict
ezsignsignergroup_create_object_v1_response_form_dict = ezsignsignergroup_create_object_v1_response.from_dict(ezsignsignergroup_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


