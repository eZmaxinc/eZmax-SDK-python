# ScimUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_name** | **str** | A service provider&#39;s unique identifier for the user, typically used by the user to directly authenticate to the service provider.  Often displayed to the user as their unique identifier within the system (as opposed to \&quot;id\&quot; or \&quot;externalId\&quot;, which are generally opaque and not user-friendly identifiers).  Each User MUST include a non-empty userName value.  This identifier MUST be unique across the service provider&#39;s entire set of Users.  This attribute is REQUIRED and is case insensitive. | 
**display_name** | **str** |  | [optional] 
**emails** | [**List[ScimEmail]**](ScimEmail.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.scim_user import ScimUser

# TODO update the JSON string below
json = "{}"
# create an instance of ScimUser from a JSON string
scim_user_instance = ScimUser.from_json(json)
# print the JSON string representation of the object
print(ScimUser.to_json())

# convert the object into a dict
scim_user_dict = scim_user_instance.to_dict()
# create an instance of ScimUser from a dict
scim_user_form_dict = scim_user.from_dict(scim_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


