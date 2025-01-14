# UsergroupGetListV1ResponseMPayload

Payload for GET /1/object/usergroup/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_row_returned** | **int** | The number of rows returned | 
**i_row_filtered** | **int** | The number of rows matching your filters (if any) or the total number of rows | 
**a_obj_usergroup** | [**List[UsergroupListElement]**](UsergroupListElement.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_get_list_v1_response_m_payload import UsergroupGetListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupGetListV1ResponseMPayload from a JSON string
usergroup_get_list_v1_response_m_payload_instance = UsergroupGetListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UsergroupGetListV1ResponseMPayload.to_json())

# convert the object into a dict
usergroup_get_list_v1_response_m_payload_dict = usergroup_get_list_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupGetListV1ResponseMPayload from a dict
usergroup_get_list_v1_response_m_payload_from_dict = UsergroupGetListV1ResponseMPayload.from_dict(usergroup_get_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


