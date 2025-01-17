# SecretquestionGetAutocompleteV2Response

Response for GET /2/object/secretquestion/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**SecretquestionGetAutocompleteV2ResponseMPayload**](SecretquestionGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.secretquestion_get_autocomplete_v2_response import SecretquestionGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of SecretquestionGetAutocompleteV2Response from a JSON string
secretquestion_get_autocomplete_v2_response_instance = SecretquestionGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(SecretquestionGetAutocompleteV2Response.to_json())

# convert the object into a dict
secretquestion_get_autocomplete_v2_response_dict = secretquestion_get_autocomplete_v2_response_instance.to_dict()
# create an instance of SecretquestionGetAutocompleteV2Response from a dict
secretquestion_get_autocomplete_v2_response_from_dict = SecretquestionGetAutocompleteV2Response.from_dict(secretquestion_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


