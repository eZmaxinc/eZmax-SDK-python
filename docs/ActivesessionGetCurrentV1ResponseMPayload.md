# ActivesessionGetCurrentV1ResponseMPayload

Payload for the /1/object/activesession/getCurrent API Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_customer_code** | **str** | The customer code specific to the client in which the API request is being made | 
**e_activesession_weekdaystart** | [**FieldEActivesessionWeekdaystart**](FieldEActivesessionWeekdaystart.md) |  | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**s_company_name_x** | **str** | The name of the active Company in the current language | 
**s_department_name_x** | **str** | The name of the active Department in the current language | 
**a_registered_modules** | **[str]** | An Array of Registered modules.  These are the modules that are Licensed to be used by the User or the API Key. | 
**a_permissions** | **[int]** | An array of permissions granted to the user or api key | 
**fki_user_id** | **int** | The unique ID of the User | 
**fki_apikey_id** | **int** | The unique ID of the Apikey | 
**e_activesession_sessiontype** | **str** | The type of session used for the API request call | defaults to "Normal"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


