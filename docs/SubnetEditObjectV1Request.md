# SubnetEditObjectV1Request

Request for PUT /1/object/subnet/{pkiSubnetID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_subnet** | [**SubnetRequestCompound**](SubnetRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.subnet_edit_object_v1_request import SubnetEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetEditObjectV1Request from a JSON string
subnet_edit_object_v1_request_instance = SubnetEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print SubnetEditObjectV1Request.to_json()

# convert the object into a dict
subnet_edit_object_v1_request_dict = subnet_edit_object_v1_request_instance.to_dict()
# create an instance of SubnetEditObjectV1Request from a dict
subnet_edit_object_v1_request_form_dict = subnet_edit_object_v1_request.from_dict(subnet_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


