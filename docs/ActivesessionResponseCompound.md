# ActivesessionResponseCompound

Payload for the /1/object/activesession/getCurrent API Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_activesession_sessiontype** | [**FieldEActivesessionSessiontype**](FieldEActivesessionSessiontype.md) |  | 
**e_activesession_weekdaystart** | [**FieldEActivesessionWeekdaystart**](FieldEActivesessionWeekdaystart.md) |  | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | 
**b_activesession_debug** | **bool** | Whether the active session is in debug or not | 
**pks_customer_code** | [**FieldPksCustomerCode**](FieldPksCustomerCode.md) |  | 
**a_pki_permission_id** | **[int]** | An array of permissions granted to the user or api key | 
**obj_user_real** | [**ActivesessionResponseCompoundUser**](ActivesessionResponseCompoundUser.md) |  | 
**a_e_module_internalname** | **[str]** | An Array of Registered modules.  These are the modules that are Licensed to be used by the User or the API Key. | 
**obj_user_cloned** | [**ActivesessionResponseCompoundUser**](ActivesessionResponseCompoundUser.md) |  | [optional] 
**obj_apikey** | [**ActivesessionResponseCompoundApikey**](ActivesessionResponseCompoundApikey.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


