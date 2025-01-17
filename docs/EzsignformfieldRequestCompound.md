# EzsignformfieldRequestCompound

An Ezsignformfield Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignelementdependency** | [**List[EzsignelementdependencyRequestCompound]**](EzsignelementdependencyRequest.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignformfield_request_compound import EzsignformfieldRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldRequestCompound from a JSON string
ezsignformfield_request_compound_instance = EzsignformfieldRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldRequestCompound.to_json())

# convert the object into a dict
ezsignformfield_request_compound_dict = ezsignformfield_request_compound_instance.to_dict()
# create an instance of EzsignformfieldRequestCompound from a dict
ezsignformfield_request_compound_from_dict = EzsignformfieldRequestCompound.from_dict(ezsignformfield_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


