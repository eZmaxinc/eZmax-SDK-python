# ContactinformationsResponseCompound

A Contactinformations Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_address** | [**List[AddressResponseCompound]**](AddressResponse.md) |  | 
**a_obj_phone** | [**List[PhoneResponseCompound]**](PhoneResponseCompound.md) |  | 
**a_obj_email** | [**List[EmailResponseCompound]**](EmailResponse.md) |  | 
**a_obj_website** | [**List[WebsiteResponseCompound]**](WebsiteResponse.md) |  | 

## Example

```python
from eZmaxApi.models.contactinformations_response_compound import ContactinformationsResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ContactinformationsResponseCompound from a JSON string
contactinformations_response_compound_instance = ContactinformationsResponseCompound.from_json(json)
# print the JSON string representation of the object
print(ContactinformationsResponseCompound.to_json())

# convert the object into a dict
contactinformations_response_compound_dict = contactinformations_response_compound_instance.to_dict()
# create an instance of ContactinformationsResponseCompound from a dict
contactinformations_response_compound_from_dict = ContactinformationsResponseCompound.from_dict(contactinformations_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


