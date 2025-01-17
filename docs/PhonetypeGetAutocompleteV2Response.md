# PhonetypeGetAutocompleteV2Response

Response for GET /2/object/phonetype/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**PhonetypeGetAutocompleteV2ResponseMPayload**](PhonetypeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.phonetype_get_autocomplete_v2_response import PhonetypeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of PhonetypeGetAutocompleteV2Response from a JSON string
phonetype_get_autocomplete_v2_response_instance = PhonetypeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(PhonetypeGetAutocompleteV2Response.to_json())

# convert the object into a dict
phonetype_get_autocomplete_v2_response_dict = phonetype_get_autocomplete_v2_response_instance.to_dict()
# create an instance of PhonetypeGetAutocompleteV2Response from a dict
phonetype_get_autocomplete_v2_response_from_dict = PhonetypeGetAutocompleteV2Response.from_dict(phonetype_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


