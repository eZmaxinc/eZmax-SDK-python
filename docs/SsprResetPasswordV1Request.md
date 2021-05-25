# SsprResetPasswordV1Request

Request for the /1/module/sspr/resetPassword API Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pks_customer_code** | [**FieldPksCustomerCode**](FieldPksCustomerCode.md) |  | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**e_user_type_sspr** | [**FieldEUserTypeSSPR**](FieldEUserTypeSSPR.md) |  | 
**bin_user_ssp_rtoken** | **str** | Hex Encoded Secret SSPR token | 
**s_password** | **str** | A Password.  Must meet complexity requirements | 
**s_email_address** | **str** | The email address. | [optional] 
**s_user_loginname** | **str** | The Login name of the User. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


