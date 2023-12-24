# ContactRequestCompound

A Contact Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_contacttitle_id** | **int** | The unique ID of the Contacttitle.  Valid values:  |Value|Description| |-|-| |1|Ms.| |2|Mr.| |4|(Blank)| |5|Me (For Notaries)| | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**s_contact_company** | **str** | The Company name of the contact | 
**dt_contact_birthdate** | **str** | The Birth Date of the contact | [optional] 
**obj_contactinformations** | [**ContactinformationsRequestCompound**](ContactinformationsRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.contact_request_compound import ContactRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ContactRequestCompound from a JSON string
contact_request_compound_instance = ContactRequestCompound.from_json(json)
# print the JSON string representation of the object
print ContactRequestCompound.to_json()

# convert the object into a dict
contact_request_compound_dict = contact_request_compound_instance.to_dict()
# create an instance of ContactRequestCompound from a dict
contact_request_compound_form_dict = contact_request_compound.from_dict(contact_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


