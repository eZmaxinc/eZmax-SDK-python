# CommonAudit

Gives informations about the user that created the object and the last user to have modified it.  If the object was never modified after creation, both Created and Modified informations will be the same.  Apikey details will only be provided if the changes were made by an API key.  

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id_created** | **int** | The unique ID of the User | 
**fki_user_id_modified** | **int** | The unique ID of the User | 
**dt_created_date** | **str** | Represent a Date Time. The timezone is the one configured in the User&#39;s profile. | 
**dt_modified_date** | **str** | Represent a Date Time. The timezone is the one configured in the User&#39;s profile. | 
**fki_apikey_id_created** | **int** | The unique ID of the Apikey | [optional] 
**fki_apikey_id_modified** | **int** | The unique ID of the Apikey | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


