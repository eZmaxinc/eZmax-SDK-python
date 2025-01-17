# EzsigntemplatepackageResponseCompound

A Ezsigntemplatepackage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackagesigner** | [**List[EzsigntemplatepackagesignerResponseCompound]**](EzsigntemplatepackagesignerResponseCompound.md) |  | 
**a_obj_ezsigntemplatepackagemembership** | [**List[EzsigntemplatepackagemembershipResponseCompound]**](EzsigntemplatepackagemembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_response_compound import EzsigntemplatepackageResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageResponseCompound from a JSON string
ezsigntemplatepackage_response_compound_instance = EzsigntemplatepackageResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageResponseCompound.to_json())

# convert the object into a dict
ezsigntemplatepackage_response_compound_dict = ezsigntemplatepackage_response_compound_instance.to_dict()
# create an instance of EzsigntemplatepackageResponseCompound from a dict
ezsigntemplatepackage_response_compound_from_dict = EzsigntemplatepackageResponseCompound.from_dict(ezsigntemplatepackage_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


