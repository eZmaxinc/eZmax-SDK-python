# SystemconfigurationtypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/systemconfigurationtype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_systemconfigurationtype** | [**List[SystemconfigurationtypeAutocompleteElementResponse]**](SystemconfigurationtypeAutocompleteElementResponse.md) | An array of Systemconfigurationtype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.systemconfigurationtype_get_autocomplete_v2_response_m_payload import SystemconfigurationtypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationtypeGetAutocompleteV2ResponseMPayload from a JSON string
systemconfigurationtype_get_autocomplete_v2_response_m_payload_instance = SystemconfigurationtypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationtypeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
systemconfigurationtype_get_autocomplete_v2_response_m_payload_dict = systemconfigurationtype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of SystemconfigurationtypeGetAutocompleteV2ResponseMPayload from a dict
systemconfigurationtype_get_autocomplete_v2_response_m_payload_from_dict = SystemconfigurationtypeGetAutocompleteV2ResponseMPayload.from_dict(systemconfigurationtype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


