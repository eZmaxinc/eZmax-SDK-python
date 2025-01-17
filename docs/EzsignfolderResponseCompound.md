# EzsignfolderResponseCompound

An Ezsignfolder Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_timezone** | [**CustomTimezoneWithCodeResponse**](CustomTimezoneWithCodeResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_response_compound import EzsignfolderResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderResponseCompound from a JSON string
ezsignfolder_response_compound_instance = EzsignfolderResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderResponseCompound.to_json())

# convert the object into a dict
ezsignfolder_response_compound_dict = ezsignfolder_response_compound_instance.to_dict()
# create an instance of EzsignfolderResponseCompound from a dict
ezsignfolder_response_compound_from_dict = EzsignfolderResponseCompound.from_dict(ezsignfolder_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


