# ContactinformationsRequestCompound

A Contactinformations Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_address_default** | **int** | The index in the a_objAddress array (zero based index) representing the Address object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_phone_default** | **int** | The index in the a_objPhone array (zero based index) representing the Phone object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_email_default** | **int** | The index in the a_objEmail array (zero based index) representing the Email object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**i_website_default** | **int** | The index in the a_objWebsite array (zero based index) representing the Website object that should become the default one.  You can leave the value to 0 if the array is empty. | 
**a_obj_address** | [**[AddressRequestCompound]**](AddressRequestCompound.md) |  | 
**a_obj_phone** | [**[PhoneRequestCompound]**](PhoneRequestCompound.md) |  | 
**a_obj_email** | [**[EmailRequestCompound]**](EmailRequestCompound.md) |  | 
**a_obj_website** | [**[WebsiteRequestCompound]**](WebsiteRequestCompound.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


