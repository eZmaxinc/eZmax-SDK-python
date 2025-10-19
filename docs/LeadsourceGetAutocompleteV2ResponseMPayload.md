# LeadsourceGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/leadsource/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_leadsource** | [**List[LeadsourceAutocompleteElementResponse]**](LeadsourceAutocompleteElementResponse.md) | An array of Leadsource autocomplete element response. | 

## Example

```python
from eZmaxApi.models.leadsource_get_autocomplete_v2_response_m_payload import LeadsourceGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LeadsourceGetAutocompleteV2ResponseMPayload from a JSON string
leadsource_get_autocomplete_v2_response_m_payload_instance = LeadsourceGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(LeadsourceGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
leadsource_get_autocomplete_v2_response_m_payload_dict = leadsource_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of LeadsourceGetAutocompleteV2ResponseMPayload from a dict
leadsource_get_autocomplete_v2_response_m_payload_from_dict = LeadsourceGetAutocompleteV2ResponseMPayload.from_dict(leadsource_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


