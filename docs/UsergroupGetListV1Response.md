# UsergroupGetListV1Response

Response for GET /1/object/usergroup/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UsergroupGetListV1ResponseMPayload**](UsergroupGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_list_v1_response import UsergroupGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetListV1Response from a JSON string
usergroup_get_list_v1_response_instance = UsergroupGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupGetListV1Response.to_json())

# convert the object into a dict
usergroup_get_list_v1_response_dict = usergroup_get_list_v1_response_instance.to_dict()
# create an instance of UsergroupGetListV1Response from a dict
usergroup_get_list_v1_response_from_dict = UsergroupGetListV1Response.from_dict(usergroup_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


