# EzsignuserResponse

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
from eZmaxApi.models.ezsignuser_response import EzsignuserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignuserResponse from a JSON string
ezsignuser_response_instance = EzsignuserResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignuserResponse.to_json())

# convert the object into a dict
ezsignuser_response_dict = ezsignuser_response_instance.to_dict()
# create an instance of EzsignuserResponse from a dict
ezsignuser_response_from_dict = EzsignuserResponse.from_dict(ezsignuser_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


