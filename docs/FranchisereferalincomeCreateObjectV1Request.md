# FranchisereferalincomeCreateObjectV1Request

Request for POST /1/object/franchisereferalincome

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_franchisereferalincome** | [**FranchisereferalincomeRequest**](FranchisereferalincomeRequest.md) |  | [optional] 
**obj_franchisereferalincome_compound** | [**FranchisereferalincomeRequestCompound**](FranchisereferalincomeRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.franchisereferalincome_create_object_v1_request import FranchisereferalincomeCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisereferalincomeCreateObjectV1Request from a JSON string
franchisereferalincome_create_object_v1_request_instance = FranchisereferalincomeCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print FranchisereferalincomeCreateObjectV1Request.to_json()

# convert the object into a dict
franchisereferalincome_create_object_v1_request_dict = franchisereferalincome_create_object_v1_request_instance.to_dict()
# create an instance of FranchisereferalincomeCreateObjectV1Request from a dict
franchisereferalincome_create_object_v1_request_form_dict = franchisereferalincome_create_object_v1_request.from_dict(franchisereferalincome_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


