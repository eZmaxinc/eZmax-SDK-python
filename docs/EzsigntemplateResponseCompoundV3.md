# EzsigntemplateResponseCompoundV3

A Ezsigntemplate Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentResponse**](EzsigntemplatedocumentResponse.md) |  | [optional] 
**a_obj_ezsigntemplatesigner** | [**List[EzsigntemplatesignerResponseCompound]**](EzsigntemplatesignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_response_compound_v3 import EzsigntemplateResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateResponseCompoundV3 from a JSON string
ezsigntemplate_response_compound_v3_instance = EzsigntemplateResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateResponseCompoundV3.to_json())

# convert the object into a dict
ezsigntemplate_response_compound_v3_dict = ezsigntemplate_response_compound_v3_instance.to_dict()
# create an instance of EzsigntemplateResponseCompoundV3 from a dict
ezsigntemplate_response_compound_v3_from_dict = EzsigntemplateResponseCompoundV3.from_dict(ezsigntemplate_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


