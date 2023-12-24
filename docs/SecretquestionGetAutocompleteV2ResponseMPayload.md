# SecretquestionGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/secretquestion/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_secretquestion** | [**List[SecretquestionAutocompleteElementResponse]**](SecretquestionAutocompleteElementResponse.md) | An array of Secretquestion autocomplete element response. | 

## Example

```python
from eZmaxApi.models.secretquestion_get_autocomplete_v2_response_m_payload import SecretquestionGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SecretquestionGetAutocompleteV2ResponseMPayload from a JSON string
secretquestion_get_autocomplete_v2_response_m_payload_instance = SecretquestionGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print SecretquestionGetAutocompleteV2ResponseMPayload.to_json()

# convert the object into a dict
secretquestion_get_autocomplete_v2_response_m_payload_dict = secretquestion_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of SecretquestionGetAutocompleteV2ResponseMPayload from a dict
secretquestion_get_autocomplete_v2_response_m_payload_form_dict = secretquestion_get_autocomplete_v2_response_m_payload.from_dict(secretquestion_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


