# UsergroupEditUsergroupdelegationsV1Request

Request for PUT /1/object/usergroup/{pkiUsergroupID}/editUsergroupdelegations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupdelegation** | [**List[UsergroupdelegationRequestCompound]**](UsergroupdelegationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_usergroupdelegations_v1_request import UsergroupEditUsergroupdelegationsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditUsergroupdelegationsV1Request from a JSON string
usergroup_edit_usergroupdelegations_v1_request_instance = UsergroupEditUsergroupdelegationsV1Request.from_json(json)
# print the JSON string representation of the object
print(UsergroupEditUsergroupdelegationsV1Request.to_json())

# convert the object into a dict
usergroup_edit_usergroupdelegations_v1_request_dict = usergroup_edit_usergroupdelegations_v1_request_instance.to_dict()
# create an instance of UsergroupEditUsergroupdelegationsV1Request from a dict
usergroup_edit_usergroupdelegations_v1_request_form_dict = usergroup_edit_usergroupdelegations_v1_request.from_dict(usergroup_edit_usergroupdelegations_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


