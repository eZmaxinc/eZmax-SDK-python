# CustomEzmaxpricingResponse

A Custom Ezmaxpricing Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxpricing_id** | **int** | The unique ID of the Ezmaxpricing | 
**d_ezmaxpricing_rebateezsignallagents** | **str** | The rebate offered when eZsign is taken for all agents | 
**dt_ezmaxpricing_start** | **str** | The start date of the Ezmaxpricing | 
**dt_ezmaxpricing_end** | **str** | The end date of the Ezmaxpricing | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezmaxpricing_response import CustomEzmaxpricingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzmaxpricingResponse from a JSON string
custom_ezmaxpricing_response_instance = CustomEzmaxpricingResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzmaxpricingResponse.to_json())

# convert the object into a dict
custom_ezmaxpricing_response_dict = custom_ezmaxpricing_response_instance.to_dict()
# create an instance of CustomEzmaxpricingResponse from a dict
custom_ezmaxpricing_response_from_dict = CustomEzmaxpricingResponse.from_dict(custom_ezmaxpricing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


