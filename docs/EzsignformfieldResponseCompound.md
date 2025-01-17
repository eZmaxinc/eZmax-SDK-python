# EzsignformfieldResponseCompound

An Ezsignformfield Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignelementdependency** | [**List[EzsignelementdependencyResponseCompound]**](EzsignelementdependencyResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignformfield_response_compound import EzsignformfieldResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldResponseCompound from a JSON string
ezsignformfield_response_compound_instance = EzsignformfieldResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldResponseCompound.to_json())

# convert the object into a dict
ezsignformfield_response_compound_dict = ezsignformfield_response_compound_instance.to_dict()
# create an instance of EzsignformfieldResponseCompound from a dict
ezsignformfield_response_compound_from_dict = EzsignformfieldResponseCompound.from_dict(ezsignformfield_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


