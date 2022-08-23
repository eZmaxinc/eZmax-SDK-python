# EzsignfoldertypeGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldertype_id** | [**FieldPkiEzsignfoldertypeID**](FieldPkiEzsignfoldertypeID.md) |  | 
**obj_ezsignfoldertype_name** | [**MultilingualEzsignfoldertypeName**](MultilingualEzsignfoldertypeName.md) |  | 
**fki_branding_id** | [**FieldPkiBrandingID**](FieldPkiBrandingID.md) |  | 
**s_branding_description_x** | **str** | The Description of the Branding in the language of the requester | 
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**i_ezsignfoldertype_archivaldays** | [**FieldIEzsignfoldertypeArchivaldays**](FieldIEzsignfoldertypeArchivaldays.md) |  | 
**e_ezsignfoldertype_disposal** | [**FieldEEzsignfoldertypeDisposal**](FieldEEzsignfoldertypeDisposal.md) |  | 
**i_ezsignfoldertype_deadlinedays** | [**FieldIEzsignfoldertypeDeadlinedays**](FieldIEzsignfoldertypeDeadlinedays.md) |  | 
**b_ezsignfoldertype_sendattatchmentsigner** | **bool** | Whether we send the Ezsigndocument and the proof as attachment in the email | 
**b_ezsignfoldertype_sendsignedtodocumentowner** | **bool** | Whether we send the signed Ezsigndocument to the Ezsigndocument&#39;s owner | 
**b_ezsignfoldertype_sendsignedtofolderowner** | **bool** | Whether we send the signed Ezsigndocument to the Ezsignfolder&#39;s owner | 
**b_ezsignfoldertype_sendsignedtocolleague** | **bool** | Whether we send the signed Ezsigndocument to the colleagues | 
**b_ezsignfoldertype_sendsummarytodocumentowner** | **bool** | Whether we send the summary to the Ezsigndocument&#39;s owner | 
**b_ezsignfoldertype_sendsummarytofolderowner** | **bool** | Whether we send the summary to the Ezsignfolder&#39;s owner | 
**b_ezsignfoldertype_sendsummarytocolleague** | **bool** | Whether we send the summary to the colleagues | 
**b_ezsignfoldertype_isactive** | **bool** | Whether the Ezsignfoldertype is active or not | 
**fki_billingentityinternal_id** | [**FieldPkiBillingentityinternalID**](FieldPkiBillingentityinternalID.md) |  | [optional] 
**fki_usergroup_id** | [**FieldPkiUsergroupID**](FieldPkiUsergroupID.md) |  | [optional] 
**fki_usergroup_id_restricted** | [**FieldPkiUsergroupID**](FieldPkiUsergroupID.md) |  | [optional] 
**fki_ezsigntsarequirement_id** | [**FieldPkiEzsigntsarequirementID**](FieldPkiEzsigntsarequirementID.md) |  | [optional] 
**s_billingentityinternal_description_x** | **str** | The description of the Billingentityinternal in the language of the requester | [optional] 
**s_ezsigntsarequirement_description_x** | **str** | The description of the Ezsigntsarequirement in the language of the requester | [optional] 
**s_email_address_signed** | **str** | The email address. | [optional] 
**s_email_address_summary** | **str** | The email address. | [optional] 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | [optional] 
**s_usergroup_name_x_restricted** | **str** | The Name of the Usergroup in the language of the requester | [optional] 
**e_ezsignfoldertype_sendreminderfrequency** | [**FieldEEzsignfoldertypeSendreminderfrequency**](FieldEEzsignfoldertypeSendreminderfrequency.md) |  | [optional] 
**i_ezsignfoldertype_disposaldays** | [**FieldIEzsignfoldertypeDisposaldays**](FieldIEzsignfoldertypeDisposaldays.md) |  | [optional] 
**b_ezsignfoldertype_sendsignedtofullgroup** | **bool** | Whether we send the signed Ezsigndocument to the Usergroup that has acces to all Ezsignfolders | [optional] 
**b_ezsignfoldertype_sendsignedtolimitedgroup** | **bool** | Whether we send the signed Ezsigndocument to the Usergroup that has acces to only their own Ezsignfolders | [optional] 
**b_ezsignfoldertype_sendsummarytofullgroup** | **bool** | Whether we send the summary to the Usergroup that has acces to all Ezsignfolders | [optional] 
**b_ezsignfoldertype_sendsummarytolimitedgroup** | **bool** | Whether we send the summary to the Usergroup that has acces to only their own Ezsignfolders | [optional] 
**a_fki_user_id_signed** | [**[FieldPkiUserID]**](FieldPkiUserID.md) |  | [optional] 
**a_fki_user_id_summary** | [**[FieldPkiUserID]**](FieldPkiUserID.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


