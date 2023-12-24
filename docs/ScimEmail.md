# ScimEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The email address. | [optional] 
**primary** | **bool** |  | [optional] 

## Example

```python
from eZmaxApi.models.scim_email import ScimEmail

# TODO update the JSON string below
json = "{}"
# create an instance of ScimEmail from a JSON string
scim_email_instance = ScimEmail.from_json(json)
# print the JSON string representation of the object
print ScimEmail.to_json()

# convert the object into a dict
scim_email_dict = scim_email_instance.to_dict()
# create an instance of ScimEmail from a dict
scim_email_form_dict = scim_email.from_dict(scim_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


