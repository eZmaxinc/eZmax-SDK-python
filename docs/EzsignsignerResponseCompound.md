# EzsignsignerResponseCompound

An Ezsignsigner Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_contact** | [**EzsignsignerResponseCompoundContact**](EzsignsignerResponseCompoundContact.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigner_response_compound import EzsignsignerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignerResponseCompound from a JSON string
ezsignsigner_response_compound_instance = EzsignsignerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignsignerResponseCompound.to_json())

# convert the object into a dict
ezsignsigner_response_compound_dict = ezsignsigner_response_compound_instance.to_dict()
# create an instance of EzsignsignerResponseCompound from a dict
ezsignsigner_response_compound_from_dict = EzsignsignerResponseCompound.from_dict(ezsignsigner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


