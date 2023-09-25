# PhoneRequestCompound

A Phone Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_phone_id** | **int** | The unique ID of the Phone. | [optional] 
**fki_phonetype_id** | **int** | The unique ID of the Phonetype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| |3|Mobile| |4|Fax| |5|Pager| |6|Toll Free| | 
**e_phone_type** | [**FieldEPhoneType**](FieldEPhoneType.md) |  | [optional] 
**s_phone_region** | **str** | The region of the phone number. (For a North America Number only)  The region is the \&quot;514\&quot; section in this sample phone number: (514) 990-1516 x123 | [optional] 
**s_phone_exchange** | **str** | The exchange of the phone number. (For a North America Number only)  The exchange is the \&quot;990\&quot; section in this sample phone number: (514) 990-1516 x123 | [optional] 
**s_phone_number** | **str** | The number of the phone number. (For a North America Number only)  The number is the \&quot;1516\&quot; section in this sample phone number: (514) 990-1516 x123 | [optional] 
**s_phone_international** | **str** | The international phone number. | [optional] 
**s_phone_extension** | **str** | The extension of the phone number.  The extension is the \&quot;123\&quot; section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 

## Example

```python
from eZmaxApi.models.phone_request_compound import PhoneRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneRequestCompound from a JSON string
phone_request_compound_instance = PhoneRequestCompound.from_json(json)
# print the JSON string representation of the object
print PhoneRequestCompound.to_json()

# convert the object into a dict
phone_request_compound_dict = phone_request_compound_instance.to_dict()
# create an instance of PhoneRequestCompound from a dict
phone_request_compound_form_dict = phone_request_compound.from_dict(phone_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


