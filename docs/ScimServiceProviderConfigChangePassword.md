# ScimServiceProviderConfigChangePassword

A complex type that specifies configuration options related to changing a password.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | A Boolean value specifying whether or not the operation is supported. | 

## Example

```python
from eZmaxApi.models.scim_service_provider_config_change_password import ScimServiceProviderConfigChangePassword

# TODO update the JSON string below
json = "{}"
# create an instance of ScimServiceProviderConfigChangePassword from a JSON string
scim_service_provider_config_change_password_instance = ScimServiceProviderConfigChangePassword.from_json(json)
# print the JSON string representation of the object
print ScimServiceProviderConfigChangePassword.to_json()

# convert the object into a dict
scim_service_provider_config_change_password_dict = scim_service_provider_config_change_password_instance.to_dict()
# create an instance of ScimServiceProviderConfigChangePassword from a dict
scim_service_provider_config_change_password_form_dict = scim_service_provider_config_change_password.from_dict(scim_service_provider_config_change_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


