# SubnetCreateObjectV1Request

Request for POST /1/object/subnet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_subnet** | [**List[SubnetRequestCompound]**](SubnetRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.subnet_create_object_v1_request import SubnetCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetCreateObjectV1Request from a JSON string
subnet_create_object_v1_request_instance = SubnetCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(SubnetCreateObjectV1Request.to_json())

# convert the object into a dict
subnet_create_object_v1_request_dict = subnet_create_object_v1_request_instance.to_dict()
# create an instance of SubnetCreateObjectV1Request from a dict
subnet_create_object_v1_request_from_dict = SubnetCreateObjectV1Request.from_dict(subnet_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


