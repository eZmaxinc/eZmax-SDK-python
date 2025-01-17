# EzsigntemplatedocumentpagerecognitionRequestCompound

A Ezsigntemplatedocumentpagerecognition Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatedocumentpagerecognition_id** | **int** | The unique ID of the Ezsigntemplatedocumentpagerecognition | [optional] 
**fki_ezsigntemplatedocumentpage_id** | **int** | The unique ID of the Ezsigntemplatedocumentpage | 
**e_ezsigntemplatedocumentpagerecognition_operator** | [**FieldEEzsigntemplatedocumentpagerecognitionOperator**](FieldEEzsigntemplatedocumentpagerecognitionOperator.md) |  | 
**e_ezsigntemplatedocumentpagerecognition_section** | [**FieldEEzsigntemplatedocumentpagerecognitionSection**](FieldEEzsigntemplatedocumentpagerecognitionSection.md) |  | 
**i_ezsigntemplatedocumentpagerecognition_similarpercentage** | **int** | The similarpercentage of the Ezsigntemplatedocumentpagerecognition | [optional] 
**i_ezsigntemplatedocumentpagerecognition_x** | **int** | The x of the Ezsigntemplatedocumentpagerecognition | [optional] 
**i_ezsigntemplatedocumentpagerecognition_y** | **int** | The y of the Ezsigntemplatedocumentpagerecognition | [optional] 
**i_ezsigntemplatedocumentpagerecognition_width** | **int** | The width of the Ezsigntemplatedocumentpagerecognition | [optional] 
**i_ezsigntemplatedocumentpagerecognition_height** | **int** | The height of the Ezsigntemplatedocumentpagerecognition | [optional] 
**t_ezsigntemplatedocumentpagerecognition_text** | **str** | The text of the Ezsigntemplatedocumentpagerecognition | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_request_compound import EzsigntemplatedocumentpagerecognitionRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentpagerecognitionRequestCompound from a JSON string
ezsigntemplatedocumentpagerecognition_request_compound_instance = EzsigntemplatedocumentpagerecognitionRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentpagerecognitionRequestCompound.to_json())

# convert the object into a dict
ezsigntemplatedocumentpagerecognition_request_compound_dict = ezsigntemplatedocumentpagerecognition_request_compound_instance.to_dict()
# create an instance of EzsigntemplatedocumentpagerecognitionRequestCompound from a dict
ezsigntemplatedocumentpagerecognition_request_compound_from_dict = EzsigntemplatedocumentpagerecognitionRequestCompound.from_dict(ezsigntemplatedocumentpagerecognition_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


