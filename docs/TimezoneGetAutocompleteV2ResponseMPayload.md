# TimezoneGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/timezone/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_timezone** | [**List[TimezoneAutocompleteElementResponse]**](TimezoneAutocompleteElementResponse.md) | An array of Timezone autocomplete element response. | 

## Example

```python
from eZmaxApi.models.timezone_get_autocomplete_v2_response_m_payload import TimezoneGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneGetAutocompleteV2ResponseMPayload from a JSON string
timezone_get_autocomplete_v2_response_m_payload_instance = TimezoneGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(TimezoneGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
timezone_get_autocomplete_v2_response_m_payload_dict = timezone_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of TimezoneGetAutocompleteV2ResponseMPayload from a dict
timezone_get_autocomplete_v2_response_m_payload_from_dict = TimezoneGetAutocompleteV2ResponseMPayload.from_dict(timezone_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


