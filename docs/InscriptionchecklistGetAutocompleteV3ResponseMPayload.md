# InscriptionchecklistGetAutocompleteV3ResponseMPayload

Payload for POST /3/object/inscriptionchecklist/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_inscriptionchecklist** | [**List[InscriptionchecklistAutocompleteElementResponse]**](InscriptionchecklistAutocompleteElementResponse.md) | An array of Inscriptionchecklist object containing the description, ID and active status about the element. | 

## Example

```python
from eZmaxApi.models.inscriptionchecklist_get_autocomplete_v3_response_m_payload import InscriptionchecklistGetAutocompleteV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionchecklistGetAutocompleteV3ResponseMPayload from a JSON string
inscriptionchecklist_get_autocomplete_v3_response_m_payload_instance = InscriptionchecklistGetAutocompleteV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionchecklistGetAutocompleteV3ResponseMPayload.to_json())

# convert the object into a dict
inscriptionchecklist_get_autocomplete_v3_response_m_payload_dict = inscriptionchecklist_get_autocomplete_v3_response_m_payload_instance.to_dict()
# create an instance of InscriptionchecklistGetAutocompleteV3ResponseMPayload from a dict
inscriptionchecklist_get_autocomplete_v3_response_m_payload_from_dict = InscriptionchecklistGetAutocompleteV3ResponseMPayload.from_dict(inscriptionchecklist_get_autocomplete_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


