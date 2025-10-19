# DomainGetAutocompleteV2Response

Response for GET /2/object/domain/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DomainGetAutocompleteV2ResponseMPayload**](DomainGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.domain_get_autocomplete_v2_response import DomainGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGetAutocompleteV2Response from a JSON string
domain_get_autocomplete_v2_response_instance = DomainGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(DomainGetAutocompleteV2Response.to_json())

# convert the object into a dict
domain_get_autocomplete_v2_response_dict = domain_get_autocomplete_v2_response_instance.to_dict()
# create an instance of DomainGetAutocompleteV2Response from a dict
domain_get_autocomplete_v2_response_from_dict = DomainGetAutocompleteV2Response.from_dict(domain_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


