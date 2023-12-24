# ScimServiceProviderConfigSort

A complex type that specifies Sort configuration options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | A Boolean value specifying whether or not sorting is supported. | 

## Example

```python
from eZmaxApi.models.scim_service_provider_config_sort import ScimServiceProviderConfigSort

# TODO update the JSON string below
json = "{}"
# create an instance of ScimServiceProviderConfigSort from a JSON string
scim_service_provider_config_sort_instance = ScimServiceProviderConfigSort.from_json(json)
# print the JSON string representation of the object
print ScimServiceProviderConfigSort.to_json()

# convert the object into a dict
scim_service_provider_config_sort_dict = scim_service_provider_config_sort_instance.to_dict()
# create an instance of ScimServiceProviderConfigSort from a dict
scim_service_provider_config_sort_form_dict = scim_service_provider_config_sort.from_dict(scim_service_provider_config_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


