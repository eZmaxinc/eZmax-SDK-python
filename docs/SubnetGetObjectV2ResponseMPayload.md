# SubnetGetObjectV2ResponseMPayload

Payload for GET /2/object/subnet/{pkiSubnetID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_subnet** | [**SubnetResponseCompound**](SubnetResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.subnet_get_object_v2_response_m_payload import SubnetGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetGetObjectV2ResponseMPayload from a JSON string
subnet_get_object_v2_response_m_payload_instance = SubnetGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SubnetGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
subnet_get_object_v2_response_m_payload_dict = subnet_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of SubnetGetObjectV2ResponseMPayload from a dict
subnet_get_object_v2_response_m_payload_from_dict = SubnetGetObjectV2ResponseMPayload.from_dict(subnet_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


