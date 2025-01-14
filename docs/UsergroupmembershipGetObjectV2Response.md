# UsergroupmembershipGetObjectV2Response

Response for GET /2/object/usergroupmembership/{pkiUsergroupmembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupmembershipGetObjectV2ResponseMPayload**](UsergroupmembershipGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupmembership_get_object_v2_response import UsergroupmembershipGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipGetObjectV2Response from a JSON string
usergroupmembership_get_object_v2_response_instance = UsergroupmembershipGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipGetObjectV2Response.to_json())

# convert the object into a dict
usergroupmembership_get_object_v2_response_dict = usergroupmembership_get_object_v2_response_instance.to_dict()
# create an instance of UsergroupmembershipGetObjectV2Response from a dict
usergroupmembership_get_object_v2_response_from_dict = UsergroupmembershipGetObjectV2Response.from_dict(usergroupmembership_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


