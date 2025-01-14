# ContactResponse

A Contact Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_contact_id** | **int** | The unique ID of the Contact | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**fki_contacttitle_id** | **int** | The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)| | 
**fki_contactinformations_id** | **int** | The unique ID of the Contactinformations | 
**dt_contact_birthdate** | **str** | The Birth Date of the contact | [optional] 
**e_contact_type** | [**FieldEContactType**](FieldEContactType.md) |  | 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**s_contact_company** | **str** | The Company name of the contact | [optional] 
**s_contact_occupation** | **str** | The occupation of the Contact | [optional] 
**t_contact_note** | **str** | The note of the Contact | [optional] 
**b_contact_isactive** | **bool** | Whether the contact is active or not | 
**obj_contactinformations** | [**ContactinformationsResponseCompound**](ContactinformationsResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.contact_response import ContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactResponse from a JSON string
contact_response_instance = ContactResponse.from_json(json)
# print the JSON string representation of the object
print(ContactResponse.to_json())

# convert the object into a dict
contact_response_dict = contact_response_instance.to_dict()
# create an instance of ContactResponse from a dict
contact_response_from_dict = ContactResponse.from_dict(contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


