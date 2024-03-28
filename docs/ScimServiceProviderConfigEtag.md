# ScimServiceProviderConfigEtag

A complex type that specifies ETag configuration options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | A Boolean value specifying whether or not the operation is supported. | 

## Example

```python
from eZmaxApi.models.scim_service_provider_config_etag import ScimServiceProviderConfigEtag

# TODO update the JSON string below
json = "{}"
# create an instance of ScimServiceProviderConfigEtag from a JSON string
scim_service_provider_config_etag_instance = ScimServiceProviderConfigEtag.from_json(json)
# print the JSON string representation of the object
print(ScimServiceProviderConfigEtag.to_json())

# convert the object into a dict
scim_service_provider_config_etag_dict = scim_service_provider_config_etag_instance.to_dict()
# create an instance of ScimServiceProviderConfigEtag from a dict
scim_service_provider_config_etag_form_dict = scim_service_provider_config_etag.from_dict(scim_service_provider_config_etag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


