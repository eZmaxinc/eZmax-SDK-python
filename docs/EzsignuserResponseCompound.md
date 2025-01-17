# EzsignuserResponseCompound

A Ezsignuser Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignuser_id** | **int** | The unique ID of the Ezsignuser | 
**fki_contact_id** | **int** | The unique ID of the Contact | 
**obj_contact** | [**ContactResponseCompound**](ContactResponseCompound.md) |  | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignuser_response_compound import EzsignuserResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignuserResponseCompound from a JSON string
ezsignuser_response_compound_instance = EzsignuserResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignuserResponseCompound.to_json())

# convert the object into a dict
ezsignuser_response_compound_dict = ezsignuser_response_compound_instance.to_dict()
# create an instance of EzsignuserResponseCompound from a dict
ezsignuser_response_compound_from_dict = EzsignuserResponseCompound.from_dict(ezsignuser_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


