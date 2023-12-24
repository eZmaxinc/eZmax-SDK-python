# CompanyGetAutocompleteV2Response

Response for GET /2/object/company/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CompanyGetAutocompleteV2ResponseMPayload**](CompanyGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.company_get_autocomplete_v2_response import CompanyGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyGetAutocompleteV2Response from a JSON string
company_get_autocomplete_v2_response_instance = CompanyGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print CompanyGetAutocompleteV2Response.to_json()

# convert the object into a dict
company_get_autocomplete_v2_response_dict = company_get_autocomplete_v2_response_instance.to_dict()
# create an instance of CompanyGetAutocompleteV2Response from a dict
company_get_autocomplete_v2_response_form_dict = company_get_autocomplete_v2_response.from_dict(company_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


