# FranchisebrokerGetAutocompleteV2Response

Response for GET /2/object/franchisebroker/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FranchisebrokerGetAutocompleteV2ResponseMPayload**](FranchisebrokerGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.franchisebroker_get_autocomplete_v2_response import FranchisebrokerGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of FranchisebrokerGetAutocompleteV2Response from a JSON string
franchisebroker_get_autocomplete_v2_response_instance = FranchisebrokerGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print FranchisebrokerGetAutocompleteV2Response.to_json()

# convert the object into a dict
franchisebroker_get_autocomplete_v2_response_dict = franchisebroker_get_autocomplete_v2_response_instance.to_dict()
# create an instance of FranchisebrokerGetAutocompleteV2Response from a dict
franchisebroker_get_autocomplete_v2_response_form_dict = franchisebroker_get_autocomplete_v2_response.from_dict(franchisebroker_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


