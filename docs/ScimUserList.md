# ScimUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_results** | **int** |  | [optional] 
**items_per_page** | **int** |  | [optional] 
**start_index** | **int** |  | [optional] 
**schemas** | **List[str]** |  | [optional] 
**resources** | [**List[ScimUser]**](ScimUser.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.scim_user_list import ScimUserList

# TODO update the JSON string below
json = "{}"
# create an instance of ScimUserList from a JSON string
scim_user_list_instance = ScimUserList.from_json(json)
# print the JSON string representation of the object
print(ScimUserList.to_json())

# convert the object into a dict
scim_user_list_dict = scim_user_list_instance.to_dict()
# create an instance of ScimUserList from a dict
scim_user_list_from_dict = ScimUserList.from_dict(scim_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


