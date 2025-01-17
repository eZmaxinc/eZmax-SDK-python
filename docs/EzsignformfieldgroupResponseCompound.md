# EzsignformfieldgroupResponseCompound

An Ezsignformfieldgroup Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignformfield** | [**List[EzsignformfieldResponseCompound]**](EzsignformfieldResponseCompound.md) |  | 
**a_obj_dropdown_element** | [**List[CustomDropdownElementResponseCompound]**](CustomDropdownElementResponse.md) |  | [optional] 
**a_obj_ezsignformfieldgroupsigner** | [**List[EzsignformfieldgroupsignerResponseCompound]**](EzsignformfieldgroupsignerResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroup_response_compound import EzsignformfieldgroupResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupResponseCompound from a JSON string
ezsignformfieldgroup_response_compound_instance = EzsignformfieldgroupResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldgroupResponseCompound.to_json())

# convert the object into a dict
ezsignformfieldgroup_response_compound_dict = ezsignformfieldgroup_response_compound_instance.to_dict()
# create an instance of EzsignformfieldgroupResponseCompound from a dict
ezsignformfieldgroup_response_compound_from_dict = EzsignformfieldgroupResponseCompound.from_dict(ezsignformfieldgroup_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


