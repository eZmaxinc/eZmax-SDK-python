# CommonResponseErrorEzsignformValidation

Generic Error Message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_error_message** | **str** | The message giving details about the error | 
**e_error_code** | [**FieldEErrorCode**](FieldEErrorCode.md) |  | 
**a_obj_ezsignformfielderror** | [**List[CustomEzsignformfielderrorResponse]**](CustomEzsignformfielderrorResponse.md) |  | 

## Example

```python
from eZmaxApi.models.common_response_error_ezsignform_validation import CommonResponseErrorEzsignformValidation

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseErrorEzsignformValidation from a JSON string
common_response_error_ezsignform_validation_instance = CommonResponseErrorEzsignformValidation.from_json(json)
# print the JSON string representation of the object
print CommonResponseErrorEzsignformValidation.to_json()

# convert the object into a dict
common_response_error_ezsignform_validation_dict = common_response_error_ezsignform_validation_instance.to_dict()
# create an instance of CommonResponseErrorEzsignformValidation from a dict
common_response_error_ezsignform_validation_form_dict = common_response_error_ezsignform_validation.from_dict(common_response_error_ezsignform_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


