# EzsigntemplateglobalResponseCompound

A Ezsigntemplateglobal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplateglobaldocument** | [**EzsigntemplateglobaldocumentResponse**](EzsigntemplateglobaldocumentResponse.md) |  | [optional] 
**a_obj_ezsigntemplateglobalsigner** | [**List[EzsigntemplateglobalsignerResponseCompound]**](EzsigntemplateglobalsignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobal_response_compound import EzsigntemplateglobalResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalResponseCompound from a JSON string
ezsigntemplateglobal_response_compound_instance = EzsigntemplateglobalResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalResponseCompound.to_json())

# convert the object into a dict
ezsigntemplateglobal_response_compound_dict = ezsigntemplateglobal_response_compound_instance.to_dict()
# create an instance of EzsigntemplateglobalResponseCompound from a dict
ezsigntemplateglobal_response_compound_from_dict = EzsigntemplateglobalResponseCompound.from_dict(ezsigntemplateglobal_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


