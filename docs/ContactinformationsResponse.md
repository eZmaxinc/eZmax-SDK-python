# ContactinformationsResponse

A Contactinformations Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_contactinformations_id** | **int** | The unique ID of the Contactinformations | 
**fki_address_id_default** | **int** | The unique ID of the Address | [optional] 
**fki_phone_id_default** | **int** | The unique ID of the Phone. | [optional] 
**fki_email_id_default** | **int** | The unique ID of the Email | [optional] 
**fki_website_id_default** | **int** | The unique ID of the Website Default | [optional] 
**e_contactinformations_type** | [**FieldEContactinformationsType**](FieldEContactinformationsType.md) |  | 
**s_contactinformations_url** | **str** | The url of the Contactinformations | [optional] 
**obj_address_default** | [**AddressResponseCompound**](AddressResponseCompound.md) |  | [optional] 
**obj_phone_default** | [**PhoneResponseCompound**](PhoneResponseCompound.md) |  | [optional] 
**obj_email_default** | [**EmailResponseCompound**](EmailResponseCompound.md) |  | [optional] 
**obj_website_default** | [**WebsiteResponseCompound**](WebsiteResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.contactinformations_response import ContactinformationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactinformationsResponse from a JSON string
contactinformations_response_instance = ContactinformationsResponse.from_json(json)
# print the JSON string representation of the object
print(ContactinformationsResponse.to_json())

# convert the object into a dict
contactinformations_response_dict = contactinformations_response_instance.to_dict()
# create an instance of ContactinformationsResponse from a dict
contactinformations_response_from_dict = ContactinformationsResponse.from_dict(contactinformations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


