# FranchiseofficeGetAutocompleteV2Response

Response for GET /2/object/franchiseoffice/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FranchiseofficeGetAutocompleteV2ResponseMPayload**](FranchiseofficeGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.franchiseoffice_get_autocomplete_v2_response import FranchiseofficeGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseofficeGetAutocompleteV2Response from a JSON string
franchiseoffice_get_autocomplete_v2_response_instance = FranchiseofficeGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(FranchiseofficeGetAutocompleteV2Response.to_json())

# convert the object into a dict
franchiseoffice_get_autocomplete_v2_response_dict = franchiseoffice_get_autocomplete_v2_response_instance.to_dict()
# create an instance of FranchiseofficeGetAutocompleteV2Response from a dict
franchiseoffice_get_autocomplete_v2_response_form_dict = franchiseoffice_get_autocomplete_v2_response.from_dict(franchiseoffice_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


