# FranchiseofficeGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/franchiseoffice/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_franchiseoffice** | [**List[FranchiseofficeAutocompleteElementResponse]**](FranchiseofficeAutocompleteElementResponse.md) | An array of Franchiseoffice autocomplete element response. | 

## Example

```python
from eZmaxApi.models.franchiseoffice_get_autocomplete_v2_response_m_payload import FranchiseofficeGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseofficeGetAutocompleteV2ResponseMPayload from a JSON string
franchiseoffice_get_autocomplete_v2_response_m_payload_instance = FranchiseofficeGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(FranchiseofficeGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
franchiseoffice_get_autocomplete_v2_response_m_payload_dict = franchiseoffice_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of FranchiseofficeGetAutocompleteV2ResponseMPayload from a dict
franchiseoffice_get_autocomplete_v2_response_m_payload_form_dict = franchiseoffice_get_autocomplete_v2_response_m_payload.from_dict(franchiseoffice_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


