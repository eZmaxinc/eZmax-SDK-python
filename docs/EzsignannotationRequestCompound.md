# EzsignannotationRequestCompound

A Ezsignannotation Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_textstylestatic** | [**TextstylestaticRequestCompound**](TextstylestaticRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignannotation_request_compound import EzsignannotationRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationRequestCompound from a JSON string
ezsignannotation_request_compound_instance = EzsignannotationRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationRequestCompound.to_json())

# convert the object into a dict
ezsignannotation_request_compound_dict = ezsignannotation_request_compound_instance.to_dict()
# create an instance of EzsignannotationRequestCompound from a dict
ezsignannotation_request_compound_from_dict = EzsignannotationRequestCompound.from_dict(ezsignannotation_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


