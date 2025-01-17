# EzsignformfieldgroupRequestCompound

An Ezsignformfieldgroup Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignformfieldgroupsigner** | [**List[EzsignformfieldgroupsignerRequestCompound]**](EzsignformfieldgroupsignerRequest.md) |  | 
**a_obj_dropdown_element** | [**List[CustomDropdownElementRequestCompound]**](CustomDropdownElementRequest.md) |  | [optional] 
**a_obj_ezsignformfield** | [**List[EzsignformfieldRequestCompound]**](EzsignformfieldRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroup_request_compound import EzsignformfieldgroupRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupRequestCompound from a JSON string
ezsignformfieldgroup_request_compound_instance = EzsignformfieldgroupRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldgroupRequestCompound.to_json())

# convert the object into a dict
ezsignformfieldgroup_request_compound_dict = ezsignformfieldgroup_request_compound_instance.to_dict()
# create an instance of EzsignformfieldgroupRequestCompound from a dict
ezsignformfieldgroup_request_compound_from_dict = EzsignformfieldgroupRequestCompound.from_dict(ezsignformfieldgroup_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


