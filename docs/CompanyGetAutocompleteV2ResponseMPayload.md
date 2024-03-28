# CompanyGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/company/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_company** | [**List[CompanyAutocompleteElementResponse]**](CompanyAutocompleteElementResponse.md) | An array of Company autocomplete element response. | 

## Example

```python
from eZmaxApi.models.company_get_autocomplete_v2_response_m_payload import CompanyGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyGetAutocompleteV2ResponseMPayload from a JSON string
company_get_autocomplete_v2_response_m_payload_instance = CompanyGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CompanyGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
company_get_autocomplete_v2_response_m_payload_dict = company_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of CompanyGetAutocompleteV2ResponseMPayload from a dict
company_get_autocomplete_v2_response_m_payload_form_dict = company_get_autocomplete_v2_response_m_payload.from_dict(company_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


