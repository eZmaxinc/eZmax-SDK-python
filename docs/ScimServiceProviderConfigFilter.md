# ScimServiceProviderConfigFilter

A complex type that specifies FILTER options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | A Boolean value specifying whether or not the operation is supported. | 
**max_results** | **int** | An integer value specifying the maximum number of resources returned in a response. | 

## Example

```python
from eZmaxApi.models.scim_service_provider_config_filter import ScimServiceProviderConfigFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ScimServiceProviderConfigFilter from a JSON string
scim_service_provider_config_filter_instance = ScimServiceProviderConfigFilter.from_json(json)
# print the JSON string representation of the object
print(ScimServiceProviderConfigFilter.to_json())

# convert the object into a dict
scim_service_provider_config_filter_dict = scim_service_provider_config_filter_instance.to_dict()
# create an instance of ScimServiceProviderConfigFilter from a dict
scim_service_provider_config_filter_form_dict = scim_service_provider_config_filter.from_dict(scim_service_provider_config_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


