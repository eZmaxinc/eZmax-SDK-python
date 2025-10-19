# DomainGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/domain/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_domain** | [**List[DomainAutocompleteElementResponse]**](DomainAutocompleteElementResponse.md) | An array of Domain autocomplete element response. | 

## Example

```python
from eZmaxApi.models.domain_get_autocomplete_v2_response_m_payload import DomainGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetAutocompleteV2ResponseMPayload from a JSON string
domain_get_autocomplete_v2_response_m_payload_instance = DomainGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DomainGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
domain_get_autocomplete_v2_response_m_payload_dict = domain_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of DomainGetAutocompleteV2ResponseMPayload from a dict
domain_get_autocomplete_v2_response_m_payload_from_dict = DomainGetAutocompleteV2ResponseMPayload.from_dict(domain_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


