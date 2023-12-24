# EzsignbulksendCreateEzsignbulksendtransmissionV1Request

Request for POST /1/object/ezsignbulksend/{pkiEzsignbulksendID}/createEzsignbulksendtransmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_userlogintype_id** | **int** | The unique ID of the Userlogintype  Valid values:  |Value|Description|Detail| |-|-|-| |1|**Email Only**|The Ezsignsigner will receive a secure link by email| |2|**Email and phone or SMS**|The Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**| |3|**Email and secret question**|The Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer| |4|**In person only**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and there won&#39;t be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type| |5|**In person with phone or SMS**|The Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**| | 
**fki_ezsigntsarequirement_id** | **int** | The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server&#39;s time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server&#39;s time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**| | [optional] 
**s_ezsignbulksendtransmission_description** | **str** | The description of the Ezsignbulksendtransmission | 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | 
**e_ezsignfolder_sendreminderfrequency** | [**FieldEEzsignfolderSendreminderfrequency**](FieldEEzsignfolderSendreminderfrequency.md) |  | 
**t_extra_message** | **str** | A custom text message that will be added to the email sent. | 
**s_csv_base64** | **bytearray** | The Base64 encoded binary content of the CSV file. | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_create_ezsignbulksendtransmission_v1_request import EzsignbulksendCreateEzsignbulksendtransmissionV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV1Request from a JSON string
ezsignbulksend_create_ezsignbulksendtransmission_v1_request_instance = EzsignbulksendCreateEzsignbulksendtransmissionV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendCreateEzsignbulksendtransmissionV1Request.to_json()

# convert the object into a dict
ezsignbulksend_create_ezsignbulksendtransmission_v1_request_dict = ezsignbulksend_create_ezsignbulksendtransmission_v1_request_instance.to_dict()
# create an instance of EzsignbulksendCreateEzsignbulksendtransmissionV1Request from a dict
ezsignbulksend_create_ezsignbulksendtransmission_v1_request_form_dict = ezsignbulksend_create_ezsignbulksendtransmission_v1_request.from_dict(ezsignbulksend_create_ezsignbulksendtransmission_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


