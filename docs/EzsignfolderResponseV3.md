# EzsignfolderResponseV3

An Ezsignfolder Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**obj_ezsignfoldertype** | [**CustomEzsignfoldertypeResponse**](CustomEzsignfoldertypeResponse.md) |  | [optional] 
**fki_timezone_id** | **int** | The unique ID of the Timezone | [optional] 
**e_ezsignfolder_completion** | [**FieldEEzsignfolderCompletion**](FieldEEzsignfolderCompletion.md) |  | 
**e_ezsignfolder_documentdependency** | [**FieldEEzsignfolderDocumentdependency**](FieldEEzsignfolderDocumentdependency.md) |  | [optional] 
**s_ezsignfoldertype_name_x** | **str** |  | [optional] 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | [optional] 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | [optional] 
**fki_ezsigntsarequirement_id** | **int** | The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server&#39;s time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server&#39;s time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**| | [optional] 
**s_ezsigntsarequirement_description_x** | **str** | The description of the Ezsigntsarequirement in the language of the requester | [optional] 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**t_ezsignfolder_note** | **str** | Note about the Ezsignfolder | [optional] 
**b_ezsignfolder_isdisposable** | **bool** | If the Ezsigndocument can be disposed | [optional] 
**i_ezsignfolder_sendreminderfirstdays** | **int** | The number of days before the the first reminder sending | [optional] 
**i_ezsignfolder_sendreminderotherdays** | **int** | The number of days after the first reminder sending | [optional] 
**dt_ezsignfolder_delayedsenddate** | **str** | The date and time at which the Ezsignfolder will be sent in the future. | [optional] 
**dt_ezsignfolder_duedate** | **str** | The maximum date and time at which the Ezsignfolder can be signed. | [optional] 
**dt_ezsignfolder_sentdate** | **str** | The date and time at which the Ezsignfolder was sent the last time. | [optional] 
**dt_ezsignfolder_scheduledarchive** | **str** | The scheduled date and time at which the Ezsignfolder should be archived. | [optional] 
**dt_ezsignfolder_scheduleddispose** | **str** | The scheduled date at which the Ezsignfolder should be Disposed. | [optional] 
**e_ezsignfolder_step** | [**FieldEEzsignfolderStep**](FieldEEzsignfolderStep.md) |  | [optional] 
**dt_ezsignfolder_close** | **str** | The date and time at which the Ezsignfolder was closed. Either by applying the last signature or by completing it prematurely. | [optional] 
**dt_ezsignfolder_archive** | **str** | The date and time at which the Ezsignfolder was archived. | [optional] 
**dt_ezsignfolder_dispose** | **str** | The date and time at which the Ezsignfolder was disposed. | [optional] 
**t_ezsignfolder_message** | **str** | A custom text message that will be added to the email sent. | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | [optional] 
**s_ezsignfolder_externalid** | **str** | This field can be used to store an External ID from the client&#39;s system.  Anything can be stored in this field, it will never be evaluated by the eZmax system and will be returned AS-IS.  To store multiple values, consider using a JSON formatted structure, a URL encoded string, a CSV or any other custom format.  | [optional] 
**e_ezsignfolder_access** | [**ComputedEEzsignfolderAccess**](ComputedEEzsignfolderAccess.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_response_v3 import EzsignfolderResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderResponseV3 from a JSON string
ezsignfolder_response_v3_instance = EzsignfolderResponseV3.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderResponseV3.to_json())

# convert the object into a dict
ezsignfolder_response_v3_dict = ezsignfolder_response_v3_instance.to_dict()
# create an instance of EzsignfolderResponseV3 from a dict
ezsignfolder_response_v3_from_dict = EzsignfolderResponseV3.from_dict(ezsignfolder_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


