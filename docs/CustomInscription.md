# CustomInscription

A custom Inscription object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_inscription_id** | **int** | The unique ID of the Inscription. | 
**fki_address_id** | **int** | The unique ID of the Address | 
**obj_address** | [**AddressResponseCompound**](AddressResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.custom_inscription import CustomInscription

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInscription from a JSON string
custom_inscription_instance = CustomInscription.from_json(json)
# print the JSON string representation of the object
print(CustomInscription.to_json())

# convert the object into a dict
custom_inscription_dict = custom_inscription_instance.to_dict()
# create an instance of CustomInscription from a dict
custom_inscription_from_dict = CustomInscription.from_dict(custom_inscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


