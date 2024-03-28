# ProvinceGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/province/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_province** | [**List[ProvinceAutocompleteElementResponse]**](ProvinceAutocompleteElementResponse.md) | An array of Province autocomplete element response. | 

## Example

```python
from eZmaxApi.models.province_get_autocomplete_v2_response_m_payload import ProvinceGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ProvinceGetAutocompleteV2ResponseMPayload from a JSON string
province_get_autocomplete_v2_response_m_payload_instance = ProvinceGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ProvinceGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
province_get_autocomplete_v2_response_m_payload_dict = province_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of ProvinceGetAutocompleteV2ResponseMPayload from a dict
province_get_autocomplete_v2_response_m_payload_form_dict = province_get_autocomplete_v2_response_m_payload.from_dict(province_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


