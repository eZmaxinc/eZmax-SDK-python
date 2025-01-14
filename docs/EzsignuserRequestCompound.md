# EzsignuserRequestCompound

A Ezsignuser Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignuser_id** | **int** | The unique ID of the Ezsignuser | [optional] 
**fki_contact_id** | **int** | The unique ID of the Contact | 
**obj_contact** | [**ContactRequestCompoundV2**](ContactRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignuser_request_compound import EzsignuserRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignuserRequestCompound from a JSON string
ezsignuser_request_compound_instance = EzsignuserRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignuserRequestCompound.to_json())

# convert the object into a dict
ezsignuser_request_compound_dict = ezsignuser_request_compound_instance.to_dict()
# create an instance of EzsignuserRequestCompound from a dict
ezsignuser_request_compound_from_dict = EzsignuserRequestCompound.from_dict(ezsignuser_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


