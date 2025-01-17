# EzsigntemplateResponseCompound

A Ezsigntemplate Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentResponse**](EzsigntemplatedocumentResponse.md) |  | [optional] 
**a_obj_ezsigntemplatesigner** | [**List[EzsigntemplatesignerResponseCompound]**](EzsigntemplatesignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_response_compound import EzsigntemplateResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateResponseCompound from a JSON string
ezsigntemplate_response_compound_instance = EzsigntemplateResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateResponseCompound.to_json())

# convert the object into a dict
ezsigntemplate_response_compound_dict = ezsigntemplate_response_compound_instance.to_dict()
# create an instance of EzsigntemplateResponseCompound from a dict
ezsigntemplate_response_compound_from_dict = EzsigntemplateResponseCompound.from_dict(ezsigntemplate_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


