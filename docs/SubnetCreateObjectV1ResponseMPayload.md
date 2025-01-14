# SubnetCreateObjectV1ResponseMPayload

Payload for POST /1/object/subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_subnet_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.subnet_create_object_v1_response_m_payload import SubnetCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetCreateObjectV1ResponseMPayload from a JSON string
subnet_create_object_v1_response_m_payload_instance = SubnetCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SubnetCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
subnet_create_object_v1_response_m_payload_dict = subnet_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of SubnetCreateObjectV1ResponseMPayload from a dict
subnet_create_object_v1_response_m_payload_from_dict = SubnetCreateObjectV1ResponseMPayload.from_dict(subnet_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


