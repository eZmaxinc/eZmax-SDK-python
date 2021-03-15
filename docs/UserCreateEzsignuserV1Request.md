# UserCreateEzsignuserV1Request

Request for the /1/module/user/createEzsignuser API Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**s_user_firstname** | **str** | The First name of the user | 
**s_user_lastname** | **str** | The Last name of the user | 
**s_email_address** | **str** | The email address. | 
**s_phone_region** | **str** | The region of the phone number. (For a North America Number only)  The region is the \&quot;514\&quot; section in this sample phone number: (514) 990-1516 x123 | 
**s_phone_exchange** | **str** | The exchange of the phone number. (For a North America Number only)  The exchange is the \&quot;990\&quot; section in this sample phone number: (514) 990-1516 x123 | 
**s_phone_number** | **str** | The number of the phone number. (For a North America Number only)  The number is the \&quot;1516\&quot; section in this sample phone number: (514) 990-1516 x123 | 
**s_phone_extension** | **str** | The extension of the phone number.  The extension is the \&quot;123\&quot; section in this sample phone number: (514) 990-1516 x123.  It can also be used with international phone numbers | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


