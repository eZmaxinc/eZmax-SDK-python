# SubnetGetObjectV2Response

Response for GET /2/object/subnet/{pkiSubnetID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SubnetGetObjectV2ResponseMPayload**](SubnetGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.subnet_get_object_v2_response import SubnetGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetGetObjectV2Response from a JSON string
subnet_get_object_v2_response_instance = SubnetGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(SubnetGetObjectV2Response.to_json())

# convert the object into a dict
subnet_get_object_v2_response_dict = subnet_get_object_v2_response_instance.to_dict()
# create an instance of SubnetGetObjectV2Response from a dict
subnet_get_object_v2_response_from_dict = SubnetGetObjectV2Response.from_dict(subnet_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


