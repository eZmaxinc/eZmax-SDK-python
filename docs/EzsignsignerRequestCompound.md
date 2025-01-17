# EzsignsignerRequestCompound

An Ezsignsigner Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_contact** | [**EzsignsignerRequestCompoundContact**](EzsignsignerRequestCompoundContact.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigner_request_compound import EzsignsignerRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignerRequestCompound from a JSON string
ezsignsigner_request_compound_instance = EzsignsignerRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignsignerRequestCompound.to_json())

# convert the object into a dict
ezsignsigner_request_compound_dict = ezsignsigner_request_compound_instance.to_dict()
# create an instance of EzsignsignerRequestCompound from a dict
ezsignsigner_request_compound_from_dict = EzsignsignerRequestCompound.from_dict(ezsignsigner_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


