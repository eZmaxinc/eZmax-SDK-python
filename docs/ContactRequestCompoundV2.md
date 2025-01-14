# ContactRequestCompoundV2

A Contact Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_contacttitle_id** | **int** | The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)| | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**e_contact_type** | [**FieldEContactType**](FieldEContactType.md) |  | 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**s_contact_company** | **str** | The Company name of the contact | [optional] 
**dt_contact_birthdate** | **str** | The Birth Date of the contact | [optional] 
**s_contact_occupation** | **str** | The occupation of the Contact | [optional] 
**t_contact_note** | **str** | The note of the Contact | [optional] 
**b_contact_isactive** | **bool** | Whether the contact is active or not | [optional] 
**obj_contactinformations** | [**ContactinformationsRequestCompoundV2**](ContactinformationsRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.contact_request_compound_v2 import ContactRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of ContactRequestCompoundV2 from a JSON string
contact_request_compound_v2_instance = ContactRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(ContactRequestCompoundV2.to_json())

# convert the object into a dict
contact_request_compound_v2_dict = contact_request_compound_v2_instance.to_dict()
# create an instance of ContactRequestCompoundV2 from a dict
contact_request_compound_v2_from_dict = ContactRequestCompoundV2.from_dict(contact_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


