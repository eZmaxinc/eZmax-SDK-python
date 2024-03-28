# CustomEzsignsignaturestatusResponse

A Ezsignsignaturestatus Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezsignsignaturestatus_steptype** | **str** | Type of step | 
**i_ezsignsignaturestatus_step** | **int** | The step at which the Ezsignsigner will be invited to sign or fill the form fields | 
**i_ezsignsignaturestatus_total** | **int** | The total number of signature or form fields the Ezsignsigner must process at the current step | 
**i_ezsignsignaturestatus_signed** | **int** | The number of signature or form fields the Ezsignsigner has already processed at the current step | 

## Example

```python
from eZmaxApi.models.custom_ezsignsignaturestatus_response import CustomEzsignsignaturestatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignsignaturestatusResponse from a JSON string
custom_ezsignsignaturestatus_response_instance = CustomEzsignsignaturestatusResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignsignaturestatusResponse.to_json())

# convert the object into a dict
custom_ezsignsignaturestatus_response_dict = custom_ezsignsignaturestatus_response_instance.to_dict()
# create an instance of CustomEzsignsignaturestatusResponse from a dict
custom_ezsignsignaturestatus_response_form_dict = custom_ezsignsignaturestatus_response.from_dict(custom_ezsignsignaturestatus_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


