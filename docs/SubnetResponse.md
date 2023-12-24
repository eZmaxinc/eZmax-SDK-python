# SubnetResponse

A Subnet Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_subnet_id** | **int** | The unique ID of the Subnet | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_apikey_id** | **int** | The unique ID of the Apikey | [optional] 
**obj_subnet_description** | [**MultilingualSubnetDescription**](MultilingualSubnetDescription.md) |  | 
**i_subnet_network** | **int** | The network of the Subnet in integer form. For example 8.8.8.0 would be 134744064 | 
**i_subnet_mask** | **int** | The mask of the Subnet  in integer form. For example 255.255.255.0 would be 4294967040 | 

## Example

```python
from eZmaxApi.models.subnet_response import SubnetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubnetResponse from a JSON string
subnet_response_instance = SubnetResponse.from_json(json)
# print the JSON string representation of the object
print SubnetResponse.to_json()

# convert the object into a dict
subnet_response_dict = subnet_response_instance.to_dict()
# create an instance of SubnetResponse from a dict
subnet_response_form_dict = subnet_response.from_dict(subnet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


