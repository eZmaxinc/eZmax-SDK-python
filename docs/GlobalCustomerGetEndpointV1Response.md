# GlobalCustomerGetEndpointV1Response

Response for GET /1/customer/{pksCustomerCode}/endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_endpoint_url** | **str** | The endpoint&#39;s URL | 

## Example

```python
from eZmaxApi.models.global_customer_get_endpoint_v1_response import GlobalCustomerGetEndpointV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalCustomerGetEndpointV1Response from a JSON string
global_customer_get_endpoint_v1_response_instance = GlobalCustomerGetEndpointV1Response.from_json(json)
# print the JSON string representation of the object
print(GlobalCustomerGetEndpointV1Response.to_json())

# convert the object into a dict
global_customer_get_endpoint_v1_response_dict = global_customer_get_endpoint_v1_response_instance.to_dict()
# create an instance of GlobalCustomerGetEndpointV1Response from a dict
global_customer_get_endpoint_v1_response_form_dict = global_customer_get_endpoint_v1_response.from_dict(global_customer_get_endpoint_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


