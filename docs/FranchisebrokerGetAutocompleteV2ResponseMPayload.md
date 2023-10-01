# FranchisebrokerGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/franchisebroker/getAutocomplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_franchisebroker** | [**List[FranchisebrokerAutocompleteElementResponse]**](FranchisebrokerAutocompleteElementResponse.md) | An array of Franchisebroker autocomplete element response. | 

## Example

```python
from eZmaxApi.models.franchisebroker_get_autocomplete_v2_response_m_payload import FranchisebrokerGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisebrokerGetAutocompleteV2ResponseMPayload from a JSON string
franchisebroker_get_autocomplete_v2_response_m_payload_instance = FranchisebrokerGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print FranchisebrokerGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
franchisebroker_get_autocomplete_v2_response_m_payload_dict = franchisebroker_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of FranchisebrokerGetAutocompleteV2ResponseMPayload from a dict
franchisebroker_get_autocomplete_v2_response_m_payload_form_dict = franchisebroker_get_autocomplete_v2_response_m_payload.from_dict(franchisebroker_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


