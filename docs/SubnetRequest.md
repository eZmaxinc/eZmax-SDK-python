# SubnetRequest

A Subnet Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_subnet_id** | **int** | The unique ID of the Subnet | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_apikey_id** | **int** | The unique ID of the Apikey | [optional] 
**obj_subnet_description** | [**MultilingualSubnetDescription**](MultilingualSubnetDescription.md) |  | 
**i_subnet_network** | **int** | The network of the Subnet in integer form. For example 8.8.8.0 would be 134744064 | 
**i_subnet_mask** | **int** | The mask of the Subnet  in integer form. For example 255.255.255.0 would be 4294967040 | 

## Example

```python
from eZmaxApi.models.subnet_request import SubnetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetRequest from a JSON string
subnet_request_instance = SubnetRequest.from_json(json)
# print the JSON string representation of the object
print(SubnetRequest.to_json())

# convert the object into a dict
subnet_request_dict = subnet_request_instance.to_dict()
# create an instance of SubnetRequest from a dict
subnet_request_form_dict = subnet_request.from_dict(subnet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


