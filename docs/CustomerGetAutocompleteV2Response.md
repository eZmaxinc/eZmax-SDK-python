# CustomerGetAutocompleteV2Response

Response for GET /2/object/customer/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CustomerGetAutocompleteV2ResponseMPayload**](CustomerGetAutocompleteV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.customer_get_autocomplete_v2_response import CustomerGetAutocompleteV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetAutocompleteV2Response from a JSON string
customer_get_autocomplete_v2_response_instance = CustomerGetAutocompleteV2Response.from_json(json)
# print the JSON string representation of the object
print(CustomerGetAutocompleteV2Response.to_json())

# convert the object into a dict
customer_get_autocomplete_v2_response_dict = customer_get_autocomplete_v2_response_instance.to_dict()
# create an instance of CustomerGetAutocompleteV2Response from a dict
customer_get_autocomplete_v2_response_from_dict = CustomerGetAutocompleteV2Response.from_dict(customer_get_autocomplete_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


