# ScimServiceProviderConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_schemes** | [**List[ScimAuthenticationScheme]**](ScimAuthenticationScheme.md) | A multi-valued complex type that specifies supported authentication scheme properties. | 
**bulk** | [**ScimServiceProviderConfigBulk**](ScimServiceProviderConfigBulk.md) |  | 
**change_password** | [**ScimServiceProviderConfigChangePassword**](ScimServiceProviderConfigChangePassword.md) |  | 
**documentation_uri** | **str** | An HTTP-addressable URL pointing to the service provider&#39;s human-consumable help documentation | 
**etag** | [**ScimServiceProviderConfigEtag**](ScimServiceProviderConfigEtag.md) |  | 
**filter** | [**ScimServiceProviderConfigFilter**](ScimServiceProviderConfigFilter.md) |  | 
**patch** | [**ScimServiceProviderConfigPatch**](ScimServiceProviderConfigPatch.md) |  | 
**sort** | [**ScimServiceProviderConfigSort**](ScimServiceProviderConfigSort.md) |  | 

## Example

```python
from eZmaxApi.models.scim_service_provider_config import ScimServiceProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScimServiceProviderConfig from a JSON string
scim_service_provider_config_instance = ScimServiceProviderConfig.from_json(json)
# print the JSON string representation of the object
print(ScimServiceProviderConfig.to_json())

# convert the object into a dict
scim_service_provider_config_dict = scim_service_provider_config_instance.to_dict()
# create an instance of ScimServiceProviderConfig from a dict
scim_service_provider_config_form_dict = scim_service_provider_config.from_dict(scim_service_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


