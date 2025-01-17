# EzsignfolderResponseCompoundV3

An Ezsignfolder Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_timezone** | [**CustomTimezoneWithCodeResponse**](CustomTimezoneWithCodeResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_response_compound_v3 import EzsignfolderResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderResponseCompoundV3 from a JSON string
ezsignfolder_response_compound_v3_instance = EzsignfolderResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderResponseCompoundV3.to_json())

# convert the object into a dict
ezsignfolder_response_compound_v3_dict = ezsignfolder_response_compound_v3_instance.to_dict()
# create an instance of EzsignfolderResponseCompoundV3 from a dict
ezsignfolder_response_compound_v3_from_dict = EzsignfolderResponseCompoundV3.from_dict(ezsignfolder_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


