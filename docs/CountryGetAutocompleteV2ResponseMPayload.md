# CountryGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/country/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_country** | [**List[CountryAutocompleteElementResponse]**](CountryAutocompleteElementResponse.md) | An array of Country autocomplete element response. | 

## Example

```python
from eZmaxApi.models.country_get_autocomplete_v2_response_m_payload import CountryGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CountryGetAutocompleteV2ResponseMPayload from a JSON string
country_get_autocomplete_v2_response_m_payload_instance = CountryGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CountryGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
country_get_autocomplete_v2_response_m_payload_dict = country_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of CountryGetAutocompleteV2ResponseMPayload from a dict
country_get_autocomplete_v2_response_m_payload_from_dict = CountryGetAutocompleteV2ResponseMPayload.from_dict(country_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


