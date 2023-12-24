# UsergroupdelegationGetObjectV2Response

Response for GET /2/object/usergroupdelegation/{pkiUsergroupdelegationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**UsergroupdelegationGetObjectV2ResponseMPayload**](UsergroupdelegationGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_get_object_v2_response import UsergroupdelegationGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationGetObjectV2Response from a JSON string
usergroupdelegation_get_object_v2_response_instance = UsergroupdelegationGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print UsergroupdelegationGetObjectV2Response.to_json()

# convert the object into a dict
usergroupdelegation_get_object_v2_response_dict = usergroupdelegation_get_object_v2_response_instance.to_dict()
# create an instance of UsergroupdelegationGetObjectV2Response from a dict
usergroupdelegation_get_object_v2_response_form_dict = usergroupdelegation_get_object_v2_response.from_dict(usergroupdelegation_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


