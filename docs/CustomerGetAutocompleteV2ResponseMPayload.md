# CustomerGetAutocompleteV2ResponseMPayload

Payload for POST /2/object/customer/getAutocomplete

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_customer** | [**List[CustomerAutocompleteElementResponse]**](CustomerAutocompleteElementResponse.md) | An array of Customer autocomplete element response. | 

## Example

```python
from eZmaxApi.models.customer_get_autocomplete_v2_response_m_payload import CustomerGetAutocompleteV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetAutocompleteV2ResponseMPayload from a JSON string
customer_get_autocomplete_v2_response_m_payload_instance = CustomerGetAutocompleteV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerGetAutocompleteV2ResponseMPayload.to_json())

# convert the object into a dict
customer_get_autocomplete_v2_response_m_payload_dict = customer_get_autocomplete_v2_response_m_payload_instance.to_dict()
# create an instance of CustomerGetAutocompleteV2ResponseMPayload from a dict
customer_get_autocomplete_v2_response_m_payload_from_dict = CustomerGetAutocompleteV2ResponseMPayload.from_dict(customer_get_autocomplete_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


