# EzsignsignergroupmembershipCreateObjectV1Response

Response for POST /1/object/ezsignsignergroupmembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignergroupmembershipCreateObjectV1ResponseMPayload**](EzsignsignergroupmembershipCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroupmembership_create_object_v1_response import EzsignsignergroupmembershipCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipCreateObjectV1Response from a JSON string
ezsignsignergroupmembership_create_object_v1_response_instance = EzsignsignergroupmembershipCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupmembershipCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignsignergroupmembership_create_object_v1_response_dict = ezsignsignergroupmembership_create_object_v1_response_instance.to_dict()
# create an instance of EzsignsignergroupmembershipCreateObjectV1Response from a dict
ezsignsignergroupmembership_create_object_v1_response_form_dict = ezsignsignergroupmembership_create_object_v1_response.from_dict(ezsignsignergroupmembership_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


