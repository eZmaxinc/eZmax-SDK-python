# CommonAuditdetail

Gives informations about the user that created the object or the last user to have modified it.  If the object was never modified after creation, both Created and Modified informations will be the same. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id** | **int** | The unique ID of the User | 
**s_user_loginname** | **str** | The Login name of the User. | 
**s_user_lastname** | **str** | The Last name of the user | 
**s_user_firstname** | **str** | The First name of the user | 
**dt_auditdetail_date** | **str** | Represent a Date Time. The timezone is the one configured in the User&#39;s profile. | 
**fki_apikey_id** | **int** | The unique ID of the Apikey | [optional] 
**s_apikey_description_x** | **str** | The description of the Apikey in the language of the requester | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


