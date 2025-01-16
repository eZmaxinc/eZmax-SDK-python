# EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload

Payload for POST /1/object/ezsigntemplatepublic/getEzsigntemplatepublicDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_branding** | [**CustomBrandingResponse**](CustomBrandingResponse.md) |  | [optional] 
**fki_userlogintype_id** | **int** | The unique ID of the Userlogintype  Valid values:  |Value|Description|Detail| |-|-|-| |1|**Email Only**|The Ezsignsigner will receive a secure link by email| |2|**Email and phone or SMS**|The Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**| |3|**Email and secret question**|The Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer| |4|**In person only**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and there won&#39;t be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type| |5|**In person with phone or SMS**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**| |6|**Embedded**|The Ezsignsigner will only be able to sign in the embedded solution. No email will be sent for invitation to sign. **Additional fee applies**|   |7|**Embedded with phone or SMS**|The Ezsignsigner will only be able to sign in the embedded solution and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**|   |8|**No validation**|The Ezsignsigner will not receive an email and won&#39;t have to validate his connection using 2 factor. **Additional fee applies**|      |9|**Sms only**|The Ezsignsigner will not receive an email but will will need to authenticate using SMS. **Additional fee applies**|      | 
**a_s_ezsigntemplatesigner_description** | **List[str]** |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload import EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload from a JSON string
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload_instance = EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload_dict = ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload from a dict
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload_from_dict = EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload.from_dict(ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


