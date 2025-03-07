# EzsignfoldertypeRequestV3

A Ezsignfoldertype Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**obj_ezsignfoldertype_name** | [**MultilingualEzsignfoldertypeName**](MultilingualEzsignfoldertypeName.md) |  | 
**fki_branding_id** | **int** | The unique ID of the Branding | 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | [optional] 
**fki_ezsigntsarequirement_id** | **int** | The unique ID of the Ezsigntsarequirement.  Determine if a Time Stamping Authority should add a timestamp on each of the signature. Valid values:  |Value|Description| |-|-| |1|No. TSA Timestamping will requested. This will make all signatures a lot faster since no round-trip to the TSA server will be required. Timestamping will be made using eZsign server&#39;s time.| |2|Best effort. Timestamping from a Time Stamping Authority will be requested but is not mandatory. In the very improbable case it cannot be completed, the timestamping will be made using eZsign server&#39;s time. **Additional fee applies**| |3|Mandatory. Timestamping from a Time Stamping Authority will be requested and is mandatory. In the very improbable case it cannot be completed, the signature will fail and the user will be asked to retry. **Additional fee applies**| | [optional] 
**fki_font_id_annotation** | **int** | The unique ID of the Font | [optional] 
**fki_font_id_formfield** | **int** | The unique ID of the Font | [optional] 
**fki_font_id_signature** | **int** | The unique ID of the Font | [optional] 
**fki_pdfalevel_id_convert** | **int** | The unique ID of the Pdfalevel | [optional] 
**a_fki_pdfalevel_id** | **List[int]** |  | [optional] 
**a_fki_userlogintype_id** | **List[int]** |  | 
**a_fki_usergroup_id_all** | **List[int]** |  | [optional] 
**a_fki_usergroup_id_restricted** | **List[int]** |  | [optional] 
**a_fki_usergroup_id_template** | **List[int]** |  | [optional] 
**e_ezsignfoldertype_documentdependency** | [**FieldEEzsignfoldertypeDocumentdependency**](FieldEEzsignfoldertypeDocumentdependency.md) |  | [optional] 
**s_email_address_signed** | **str** | The email address. | [optional] 
**s_email_address_summary** | **str** | The email address. | [optional] 
**e_ezsignfoldertype_pdfarequirement** | [**FieldEEzsignfoldertypePdfarequirement**](FieldEEzsignfoldertypePdfarequirement.md) |  | [optional] 
**e_ezsignfoldertype_pdfanoncompliantaction** | [**FieldEEzsignfoldertypePdfanoncompliantaction**](FieldEEzsignfoldertypePdfanoncompliantaction.md) |  | [optional] 
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**i_ezsignfoldertype_fontsizeannotation** | **int** | Font size for annotations | [optional] 
**i_ezsignfoldertype_fontsizeformfield** | **int** | Font size for form fields | [optional] 
**i_ezsignfoldertype_sendreminderfirstdays** | **int** | The number of days before the the first reminder sending | [optional] 
**i_ezsignfoldertype_sendreminderotherdays** | **int** | The number of days after the first reminder sending | [optional] 
**i_ezsignfoldertype_archivaldays** | **int** | The number of days before the archival of Ezsignfolders created using this Ezsignfoldertype | 
**e_ezsignfoldertype_disposal** | [**FieldEEzsignfoldertypeDisposal**](FieldEEzsignfoldertypeDisposal.md) |  | 
**e_ezsignfoldertype_completion** | [**FieldEEzsignfoldertypeCompletion**](FieldEEzsignfoldertypeCompletion.md) |  | 
**i_ezsignfoldertype_disposaldays** | **int** | The number of days after the archival before the disposal of the Ezsignfolder | [optional] 
**i_ezsignfoldertype_deadlinedays** | **int** | The number of days to get all Ezsignsignatures | 
**b_ezsignfoldertype_prematurelyendautomatically** | **bool** | Wheter if document will be ended prematurely after Ezsignfolder expires. | [optional] 
**i_ezsignfoldertype_prematurelyendautomaticallydays** | **int** | Number of days between Ezsignfolder expiration and automatic prematurely end of Ezsigndocuments. | [optional] 
**b_ezsignfoldertype_automaticsignature** | **bool** | Whether we allow the automatic signature by an User | [optional] 
**b_ezsignfoldertype_delegate** | **bool** | Wheter if delegation of signature is allowed to another user or not | [optional] 
**b_ezsignfoldertype_discussion** | **bool** | Wheter if creating a new Discussion is allowed or not | [optional] 
**b_ezsignfoldertype_logrecipientinproof** | **bool** | Whether we log recipient of signed document in proof | [optional] 
**b_ezsignfoldertype_reassignezsignsigner** | **bool** | Wheter if Reassignment of signature is allowed by a signatory to another signatory or not | [optional] 
**b_ezsignfoldertype_reassignuser** | **bool** | Wheter if Reassignment of signature is allowed by a user to a signatory or another user or not | [optional] 
**b_ezsignfoldertype_reassigngroup** | **bool** | Wheter if Reassignment of signatures of the groups to which the user belongs is authorized by a user to himself | [optional] 
**b_ezsignfoldertype_sendsignedtoezsignsigner** | **bool** | Whether we send an email to Ezsignsigner  when document is completed | [optional] 
**b_ezsignfoldertype_sendsignedtouser** | **bool** | Whether we send an email to User who signed when document is completed | [optional] 
**b_ezsignfoldertype_sendattachmentezsignsigner** | **bool** | Whether we send the Ezsigndocument in the email to Ezsignsigner | [optional] 
**b_ezsignfoldertype_sendproofezsignsigner** | **bool** | Whether we send the proof in the email to Ezsignsigner | [optional] 
**b_ezsignfoldertype_sendattachmentuser** | **bool** | Whether we send the Ezsigndocument in the email to User | [optional] 
**b_ezsignfoldertype_sendproofuser** | **bool** | Whether we send the proof in the email to User | [optional] 
**b_ezsignfoldertype_sendproofemail** | **bool** | Whether we send the proof in the email to external recipient | [optional] 
**b_ezsignfoldertype_allowdownloadattachmentezsignsigner** | **bool** | Whether we allow the Ezsigndocument to be downloaded by an Ezsignsigner | [optional] 
**b_ezsignfoldertype_allowdownloadproofezsignsigner** | **bool** | Whether we allow the proof to be downloaded by an Ezsignsigner | [optional] 
**b_ezsignfoldertype_sendproofreceivealldocument** | **bool** | Whether we send the proof to user and Ezsignsigner who receive all documents. | [optional] 
**b_ezsignfoldertype_sendsignedtodocumentowner** | **bool** | Whether we send the signed Ezsigndocument to the Ezsigndocument&#39;s owner | 
**b_ezsignfoldertype_sendsignedtofolderowner** | **bool** | Whether we send the signed Ezsigndocument to the Ezsignfolder&#39;s owner | 
**b_ezsignfoldertype_sendsignedtofullgroup** | **bool** | Whether we send the signed Ezsigndocument to the Usergroup that has acces to all Ezsignfolders | [optional] 
**b_ezsignfoldertype_sendsignedtolimitedgroup** | **bool** | THIS FIELD WILL BE DELETED. Whether we send the signed Ezsigndocument to the Usergroup that has acces to only their own Ezsignfolders | [optional] 
**b_ezsignfoldertype_sendsignedtocolleague** | **bool** | Whether we send the signed Ezsigndocument to the colleagues | 
**b_ezsignfoldertype_sendsummarytodocumentowner** | **bool** | Whether we send the summary to the Ezsigndocument&#39;s owner | 
**b_ezsignfoldertype_sendsummarytofolderowner** | **bool** | Whether we send the summary to the Ezsignfolder&#39;s owner | 
**b_ezsignfoldertype_sendsummarytofullgroup** | **bool** | Whether we send the summary to the Usergroup that has acces to all Ezsignfolders | [optional] 
**b_ezsignfoldertype_sendsummarytolimitedgroup** | **bool** | Whether we send the summary to the Usergroup that has acces to only their own Ezsignfolders | [optional] 
**b_ezsignfoldertype_sendsummarytocolleague** | **bool** | Whether we send the summary to the colleagues | 
**e_ezsignfoldertype_signeraccess** | [**FieldEEzsignfoldertypeSigneraccess**](FieldEEzsignfoldertypeSigneraccess.md) |  | [optional] 
**b_ezsignfoldertype_isactive** | **bool** | Whether the Ezsignfoldertype is active or not | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_request_v3 import EzsignfoldertypeRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeRequestV3 from a JSON string
ezsignfoldertype_request_v3_instance = EzsignfoldertypeRequestV3.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeRequestV3.to_json())

# convert the object into a dict
ezsignfoldertype_request_v3_dict = ezsignfoldertype_request_v3_instance.to_dict()
# create an instance of EzsignfoldertypeRequestV3 from a dict
ezsignfoldertype_request_v3_from_dict = EzsignfoldertypeRequestV3.from_dict(ezsignfoldertype_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


