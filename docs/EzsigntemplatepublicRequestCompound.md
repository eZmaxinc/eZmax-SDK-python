# EzsigntemplatepublicRequestCompound

A Ezsigntemplatepublic Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepublic_id** | **int** | The unique ID of the Ezsigntemplatepublic | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_userlogintype_id** | **int** | The unique ID of the Userlogintype  Valid values:  |Value|Description|Detail| |-|-|-| |1|**Email Only**|The Ezsignsigner will receive a secure link by email| |2|**Email and phone or SMS**|The Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**| |3|**Email and secret question**|The Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer| |4|**In person only**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and there won&#39;t be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type| |5|**In person with phone or SMS**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**| |6|**Embedded**|The Ezsignsigner will only be able to sign in the embedded solution. No email will be sent for invitation to sign. **Additional fee applies**|   |7|**Embedded with phone or SMS**|The Ezsignsigner will only be able to sign in the embedded solution and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**|   |8|**No validation**|The Ezsignsigner will not receive an email and won&#39;t have to validate his connection using 2 factor. **Additional fee applies**|      |9|**Sms only**|The Ezsignsigner will not receive an email but will will need to authenticate using SMS. **Additional fee applies**|      | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | [optional] 
**s_ezsigntemplatepublic_description** | **str** | The description of the Ezsigntemplatepublic | 
**b_ezsigntemplatepublic_isactive** | **bool** | Whether the ezsigntemplatepublic is active or not | 
**t_ezsigntemplatepublic_note** | **str** | The note of the Ezsigntemplatepublic | 
**e_ezsigntemplatepublic_limittype** | [**FieldEEzsigntemplatepublicLimittype**](FieldEEzsigntemplatepublicLimittype.md) |  | 
**i_ezsigntemplatepublic_limit** | **int** | The limit of the Ezsigntemplatepublic | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_request_compound import EzsigntemplatepublicRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicRequestCompound from a JSON string
ezsigntemplatepublic_request_compound_instance = EzsigntemplatepublicRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicRequestCompound.to_json())

# convert the object into a dict
ezsigntemplatepublic_request_compound_dict = ezsigntemplatepublic_request_compound_instance.to_dict()
# create an instance of EzsigntemplatepublicRequestCompound from a dict
ezsigntemplatepublic_request_compound_from_dict = EzsigntemplatepublicRequestCompound.from_dict(ezsigntemplatepublic_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


