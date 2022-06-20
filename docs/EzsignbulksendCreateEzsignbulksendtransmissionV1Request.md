# EzsignbulksendCreateEzsignbulksendtransmissionV1Request

Request for POST /1/object/ezsignbulksend/{pkiEzsignbulksendID}/createEzsignbulksendtransmission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_userlogintype_id** | [**FieldPkiUserlogintypeID**](FieldPkiUserlogintypeID.md) |  | 
**s_ezsignbulksendtransmission_description** | **str** | The description of the Ezsignbulksendtransmission | 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | 
**e_ezsignfolder_sendreminderfrequency** | [**FieldEEzsignfolderSendreminderfrequency**](FieldEEzsignfolderSendreminderfrequency.md) |  | 
**t_extra_message** | **str** | A custom text message that will be added to the email sent. | 
**s_csv_base64** | **str** | The Base64 encoded binary content of the CSV file. | 
**fki_ezsigntsarequirement_id** | [**FieldPkiEzsigntsarequirementID**](FieldPkiEzsigntsarequirementID.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


