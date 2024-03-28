# ScimAuthenticationScheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the authentication scheme. | 
**name** | **str** | The common authentication scheme name | 
**type** | **str** | The authentication scheme. | 

## Example

```python
from eZmaxApi.models.scim_authentication_scheme import ScimAuthenticationScheme

# TODO update the JSON string below
json = "{}"
# create an instance of ScimAuthenticationScheme from a JSON string
scim_authentication_scheme_instance = ScimAuthenticationScheme.from_json(json)
# print the JSON string representation of the object
print(ScimAuthenticationScheme.to_json())

# convert the object into a dict
scim_authentication_scheme_dict = scim_authentication_scheme_instance.to_dict()
# create an instance of ScimAuthenticationScheme from a dict
scim_authentication_scheme_form_dict = scim_authentication_scheme.from_dict(scim_authentication_scheme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


