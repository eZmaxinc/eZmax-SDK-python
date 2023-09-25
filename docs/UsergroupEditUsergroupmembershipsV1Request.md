# UsergroupEditUsergroupmembershipsV1Request

Request for PUT /1/object/usergroup/{pkiUsergroupID}/editUsergroupmemberships

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupmembership** | [**List[UsergroupmembershipRequestCompound]**](UsergroupmembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_usergroupmemberships_v1_request import UsergroupEditUsergroupmembershipsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditUsergroupmembershipsV1Request from a JSON string
usergroup_edit_usergroupmemberships_v1_request_instance = UsergroupEditUsergroupmembershipsV1Request.from_json(json)
# print the JSON string representation of the object
print UsergroupEditUsergroupmembershipsV1Request.to_json()

# convert the object into a dict
usergroup_edit_usergroupmemberships_v1_request_dict = usergroup_edit_usergroupmemberships_v1_request_instance.to_dict()
# create an instance of UsergroupEditUsergroupmembershipsV1Request from a dict
usergroup_edit_usergroupmemberships_v1_request_form_dict = usergroup_edit_usergroupmemberships_v1_request.from_dict(usergroup_edit_usergroupmemberships_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


