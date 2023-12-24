# FranchisereferalincomeCreateObjectV2Request

Request for POST /2/object/franchisereferalincome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_franchisereferalincome** | [**List[FranchisereferalincomeRequestCompound]**](FranchisereferalincomeRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.franchisereferalincome_create_object_v2_request import FranchisereferalincomeCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisereferalincomeCreateObjectV2Request from a JSON string
franchisereferalincome_create_object_v2_request_instance = FranchisereferalincomeCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print FranchisereferalincomeCreateObjectV2Request.to_json()

# convert the object into a dict
franchisereferalincome_create_object_v2_request_dict = franchisereferalincome_create_object_v2_request_instance.to_dict()
# create an instance of FranchisereferalincomeCreateObjectV2Request from a dict
franchisereferalincome_create_object_v2_request_form_dict = franchisereferalincome_create_object_v2_request.from_dict(franchisereferalincome_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


