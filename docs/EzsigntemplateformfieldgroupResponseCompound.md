# EzsigntemplateformfieldgroupResponseCompound

A Ezsigntemplateformfieldgroup Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplateformfieldgroupsigner** | [**List[EzsigntemplateformfieldgroupsignerResponseCompound]**](EzsigntemplateformfieldgroupsignerResponse.md) |  | 
**a_obj_dropdown_element** | [**List[CustomDropdownElementResponseCompound]**](CustomDropdownElementResponse.md) |  | [optional] 
**a_obj_ezsigntemplateformfield** | [**List[EzsigntemplateformfieldResponseCompound]**](EzsigntemplateformfieldResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_response_compound import EzsigntemplateformfieldgroupResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupResponseCompound from a JSON string
ezsigntemplateformfieldgroup_response_compound_instance = EzsigntemplateformfieldgroupResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateformfieldgroupResponseCompound.to_json())

# convert the object into a dict
ezsigntemplateformfieldgroup_response_compound_dict = ezsigntemplateformfieldgroup_response_compound_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupResponseCompound from a dict
ezsigntemplateformfieldgroup_response_compound_from_dict = EzsigntemplateformfieldgroupResponseCompound.from_dict(ezsigntemplateformfieldgroup_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


