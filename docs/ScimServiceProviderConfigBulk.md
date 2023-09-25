# ScimServiceProviderConfigBulk

A complex type that specifies bulk configuration options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | A Boolean value specifying whether or not the operation is supported. | 
**max_operations** | **int** | An integer value specifying the maximum number of operations. | 
**max_payload_size** | **int** | An integer value specifying the maximum payload size in bytes. | 

## Example

```python
from eZmaxApi.models.scim_service_provider_config_bulk import ScimServiceProviderConfigBulk

# TODO update the JSON string below
json = "{}"
# create an instance of ScimServiceProviderConfigBulk from a JSON string
scim_service_provider_config_bulk_instance = ScimServiceProviderConfigBulk.from_json(json)
# print the JSON string representation of the object
print ScimServiceProviderConfigBulk.to_json()

# convert the object into a dict
scim_service_provider_config_bulk_dict = scim_service_provider_config_bulk_instance.to_dict()
# create an instance of ScimServiceProviderConfigBulk from a dict
scim_service_provider_config_bulk_form_dict = scim_service_provider_config_bulk.from_dict(scim_service_provider_config_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


