# ContactinformationsRequestCompound

A Contactinformations Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_address** | [**List[AddressRequestCompound]**](AddressRequest.md) |  | 
**a_obj_phone** | [**List[PhoneRequestCompound]**](PhoneRequest.md) |  | 
**a_obj_email** | [**List[EmailRequestCompound]**](EmailRequest.md) |  | 
**a_obj_website** | [**List[WebsiteRequestCompound]**](WebsiteRequest.md) |  | 

## Example

```python
from eZmaxApi.models.contactinformations_request_compound import ContactinformationsRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ContactinformationsRequestCompound from a JSON string
contactinformations_request_compound_instance = ContactinformationsRequestCompound.from_json(json)
# print the JSON string representation of the object
print(ContactinformationsRequestCompound.to_json())

# convert the object into a dict
contactinformations_request_compound_dict = contactinformations_request_compound_instance.to_dict()
# create an instance of ContactinformationsRequestCompound from a dict
contactinformations_request_compound_from_dict = ContactinformationsRequestCompound.from_dict(contactinformations_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


