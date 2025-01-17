# EzmaxinvoicingGetAutocompleteV2Response

Response for GET /2/object/ezmaxinvoicing/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzmaxinvoicingGetAutocompleteV2ResponseMPayload**](EzmaxinvoicingGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicing_get_autocomplete_v2_response import EzmaxinvoicingGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicingGetAutocompleteV2Response from a JSON string
ezmaxinvoicing_get_autocomplete_v2_response_instance = EzmaxinvoicingGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicingGetAutocompleteV2Response.to_json())

# convert the object into a dict
ezmaxinvoicing_get_autocomplete_v2_response_dict = ezmaxinvoicing_get_autocomplete_v2_response_instance.to_dict()
# create an instance of EzmaxinvoicingGetAutocompleteV2Response from a dict
ezmaxinvoicing_get_autocomplete_v2_response_from_dict = EzmaxinvoicingGetAutocompleteV2Response.from_dict(ezmaxinvoicing_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


