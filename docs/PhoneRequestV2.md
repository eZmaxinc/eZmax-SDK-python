# PhoneRequestV2

A Phone Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_phone_id** | **int** | The unique ID of the Phone. | [optional] 
**fki_phonetype_id** | **int** | The unique ID of the Phonetype.  Valid values:  |Value|Description| |-|-| |1|Office| |2|Home| |3|Mobile| |4|Fax| |5|Pager| |6|Toll Free| | 
**s_phone_extension** | **str** | The extension of the phone number.  The extension is the \&quot;123\&quot; section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 

## Example

```python
from eZmaxApi.models.phone_request_v2 import PhoneRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneRequestV2 from a JSON string
phone_request_v2_instance = PhoneRequestV2.from_json(json)
# print the JSON string representation of the object
print(PhoneRequestV2.to_json())

# convert the object into a dict
phone_request_v2_dict = phone_request_v2_instance.to_dict()
# create an instance of PhoneRequestV2 from a dict
phone_request_v2_form_dict = phone_request_v2.from_dict(phone_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


