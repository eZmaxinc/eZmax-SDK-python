# EzsigntemplateformfieldgroupRequestCompound

A Ezsigntemplateformfieldgroup Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplateformfieldgroupsigner** | [**List[EzsigntemplateformfieldgroupsignerRequestCompound]**](EzsigntemplateformfieldgroupsignerRequest.md) |  | 
**a_obj_dropdown_element** | [**List[CustomDropdownElementRequestCompound]**](CustomDropdownElementRequest.md) |  | [optional] 
**a_obj_ezsigntemplateformfield** | [**List[EzsigntemplateformfieldRequestCompound]**](EzsigntemplateformfieldRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_request_compound import EzsigntemplateformfieldgroupRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupRequestCompound from a JSON string
ezsigntemplateformfieldgroup_request_compound_instance = EzsigntemplateformfieldgroupRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateformfieldgroupRequestCompound.to_json())

# convert the object into a dict
ezsigntemplateformfieldgroup_request_compound_dict = ezsigntemplateformfieldgroup_request_compound_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupRequestCompound from a dict
ezsigntemplateformfieldgroup_request_compound_from_dict = EzsigntemplateformfieldgroupRequestCompound.from_dict(ezsigntemplateformfieldgroup_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


