# EzsignuserRequest

A Ezsignuser Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignuser_id** | **int** | The unique ID of the Ezsignuser | [optional] 
**fki_contact_id** | **int** | The unique ID of the Contact | 
**obj_contact** | [**ContactRequestCompoundV2**](ContactRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignuser_request import EzsignuserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignuserRequest from a JSON string
ezsignuser_request_instance = EzsignuserRequest.from_json(json)
# print the JSON string representation of the object
print(EzsignuserRequest.to_json())

# convert the object into a dict
ezsignuser_request_dict = ezsignuser_request_instance.to_dict()
# create an instance of EzsignuserRequest from a dict
ezsignuser_request_from_dict = EzsignuserRequest.from_dict(ezsignuser_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


