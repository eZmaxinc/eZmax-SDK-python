# FranchisereferalincomeRequestCompound

A Franchisereferalincome Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_address** | [**AddressRequest**](AddressRequest.md) |  | [optional] 
**a_obj_contact** | [**List[ContactRequestCompound]**](ContactRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.franchisereferalincome_request_compound import FranchisereferalincomeRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisereferalincomeRequestCompound from a JSON string
franchisereferalincome_request_compound_instance = FranchisereferalincomeRequestCompound.from_json(json)
# print the JSON string representation of the object
print(FranchisereferalincomeRequestCompound.to_json())

# convert the object into a dict
franchisereferalincome_request_compound_dict = franchisereferalincome_request_compound_instance.to_dict()
# create an instance of FranchisereferalincomeRequestCompound from a dict
franchisereferalincome_request_compound_from_dict = FranchisereferalincomeRequestCompound.from_dict(franchisereferalincome_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


