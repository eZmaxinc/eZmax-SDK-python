# PeriodGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/period/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_period** | [**List[PeriodAutocompleteElementResponse]**](PeriodAutocompleteElementResponse.md) | An array of Period autocomplete element response. | 

## Example

```python
from eZmaxApi.models.period_get_autocomplete_v2_response_m_payload import PeriodGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodGetAutocompleteV2ResponseMPayload from a JSON string
period_get_autocomplete_v2_response_m_payload_instance = PeriodGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print PeriodGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
period_get_autocomplete_v2_response_m_payload_dict = period_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of PeriodGetAutocompleteV2ResponseMPayload from a dict
period_get_autocomplete_v2_response_m_payload_form_dict = period_get_autocomplete_v2_response_m_payload.from_dict(period_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


