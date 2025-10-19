# AgenttypeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/agenttype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_agenttype** | [**List[AgenttypeAutocompleteElementResponse]**](AgenttypeAutocompleteElementResponse.md) | An array of Agenttype autocomplete element response. | 

## Example

```python
from eZmaxApi.models.agenttype_get_autocomplete_v2_response_m_payload import AgenttypeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AgenttypeGetAutocompleteV2ResponseMPayload from a JSON string
agenttype_get_autocomplete_v2_response_m_payload_instance = AgenttypeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AgenttypeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
agenttype_get_autocomplete_v2_response_m_payload_dict = agenttype_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of AgenttypeGetAutocompleteV2ResponseMPayload from a dict
agenttype_get_autocomplete_v2_response_m_payload_from_dict = AgenttypeGetAutocompleteV2ResponseMPayload.from_dict(agenttype_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


