# EzsignsignerRequestCompoundContact

A Ezsignsigner->Contact Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_email_address** | **str** | The email address. | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**s_phone_extension** | **str** | The extension of the phone number.  The extension is the \&quot;123\&quot; section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers | [optional] 
**s_phone_e164_cell** | **str** | A phone number in E.164 Format | [optional] 
**s_phone_number** | **str** |  | [optional] 
**s_phone_number_cell** | **str** |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsigner_request_compound_contact import EzsignsignerRequestCompoundContact

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignerRequestCompoundContact from a JSON string
ezsignsigner_request_compound_contact_instance = EzsignsignerRequestCompoundContact.from_json(json)
# print the JSON string representation of the object
print(EzsignsignerRequestCompoundContact.to_json())

# convert the object into a dict
ezsignsigner_request_compound_contact_dict = ezsignsigner_request_compound_contact_instance.to_dict()
# create an instance of EzsignsignerRequestCompoundContact from a dict
ezsignsigner_request_compound_contact_from_dict = EzsignsignerRequestCompoundContact.from_dict(ezsignsigner_request_compound_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


