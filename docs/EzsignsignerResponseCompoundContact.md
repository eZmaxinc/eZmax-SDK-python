# EzsignsignerResponseCompoundContact

A Ezsignsigner->Contact Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_contact_id** | **int** | The unique ID of the Contact | 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_email_address** | **str** | The email address. | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**s_phone_extension** | **str** | The extension of the phone number.  The extension is the \&quot;123\&quot; section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers | [optional] 
**s_phone_e164_cell** | **str** | A phone number in E.164 Format | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsigner_response_compound_contact import EzsignsignerResponseCompoundContact

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignerResponseCompoundContact from a JSON string
ezsignsigner_response_compound_contact_instance = EzsignsignerResponseCompoundContact.from_json(json)
# print the JSON string representation of the object
print EzsignsignerResponseCompoundContact.to_json()

# convert the object into a dict
ezsignsigner_response_compound_contact_dict = ezsignsigner_response_compound_contact_instance.to_dict()
# create an instance of EzsignsignerResponseCompoundContact from a dict
ezsignsigner_response_compound_contact_form_dict = ezsignsigner_response_compound_contact.from_dict(ezsignsigner_response_compound_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


