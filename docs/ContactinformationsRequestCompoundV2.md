# ContactinformationsRequestCompoundV2

A Contactinformations Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_contactinformations_type** | [**FieldEContactinformationsType**](FieldEContactinformationsType.md) |  | 
**i_address_default** | **int** | The index in the a_objAddress array (zero based index) representing the Address object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_phone_default** | **int** | The index in the a_objPhone array (zero based index) representing the Phone object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_email_default** | **int** | The index in the a_objEmail array (zero based index) representing the Email object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_website_default** | **int** | The index in the a_objWebsite array (zero based index) representing the Website object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**a_obj_address** | [**List[AddressRequestCompound]**](AddressRequest.md) |  | 
**a_obj_phone** | [**List[PhoneRequestCompound]**](PhoneRequest.md) |  | 
**a_obj_email** | [**List[EmailRequestCompound]**](EmailRequest.md) |  | 
**a_obj_website** | [**List[WebsiteRequestCompound]**](WebsiteRequest.md) |  | 

## Example

```python
from eZmaxApi.models.contactinformations_request_compound_v2 import ContactinformationsRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of ContactinformationsRequestCompoundV2 from a JSON string
contactinformations_request_compound_v2_instance = ContactinformationsRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(ContactinformationsRequestCompoundV2.to_json())

# convert the object into a dict
contactinformations_request_compound_v2_dict = contactinformations_request_compound_v2_instance.to_dict()
# create an instance of ContactinformationsRequestCompoundV2 from a dict
contactinformations_request_compound_v2_from_dict = ContactinformationsRequestCompoundV2.from_dict(contactinformations_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


