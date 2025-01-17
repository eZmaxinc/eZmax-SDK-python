# CreditcardclientGetAutocompleteV2Response

Response for GET /2/object/creditcardclient/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CreditcardclientGetAutocompleteV2ResponseMPayload**](CreditcardclientGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.creditcardclient_get_autocomplete_v2_response import CreditcardclientGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreditcardclientGetAutocompleteV2Response from a JSON string
creditcardclient_get_autocomplete_v2_response_instance = CreditcardclientGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(CreditcardclientGetAutocompleteV2Response.to_json())

# convert the object into a dict
creditcardclient_get_autocomplete_v2_response_dict = creditcardclient_get_autocomplete_v2_response_instance.to_dict()
# create an instance of CreditcardclientGetAutocompleteV2Response from a dict
creditcardclient_get_autocomplete_v2_response_from_dict = CreditcardclientGetAutocompleteV2Response.from_dict(creditcardclient_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


