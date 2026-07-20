# ScimServiceProviderConfigPatch

A complex type that specifies PATCH configuration options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | A Boolean value specifying whether or not the operation is supported. | 

## Example

```python
from eZmaxApi.models.scim_service_provider_config_patch import ScimServiceProviderConfigPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ScimServiceProviderConfigPatch from a JSON string
scim_service_provider_config_patch_instance = ScimServiceProviderConfigPatch.from_json(json)
# print the JSON string representation of the object
print(ScimServiceProviderConfigPatch.to_json())

# convert the object into a dict
scim_service_provider_config_patch_dict = scim_service_provider_config_patch_instance.to_dict()
# create an instance of ScimServiceProviderConfigPatch from a dict
scim_service_provider_config_patch_from_dict = ScimServiceProviderConfigPatch.from_dict(scim_service_provider_config_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


