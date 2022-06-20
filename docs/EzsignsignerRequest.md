# EzsignsignerRequest

An Ezsignsigner Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_taxassignment_id** | [**FieldPkiTaxassignmentID**](FieldPkiTaxassignmentID.md) |  | 
**fki_userlogintype_id** | [**FieldPkiUserlogintypeID**](FieldPkiUserlogintypeID.md) |  | [optional] 
**fki_secretquestion_id** | [**FieldPkiSecretquestionID**](FieldPkiSecretquestionID.md) |  | [optional] 
**e_ezsignsigner_logintype** | **str** | The method the Ezsignsigner will authenticate to the signing platform.  1. **Password** means the Ezsignsigner will receive a secure link by email. 2. **PasswordPhone** means the Ezsignsigner will receive a secure link by email and will need to authenticate using SMS or Phone call. **Additional fee applies**. 3. **PasswordQuestion** means the Ezsignsigner will receive a secure link by email and will need to authenticate using a predefined question and answer. 4. **InPersonPhone** means the Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and will need to authenticate using SMS or Phone call. No email will be sent for invitation to sign. **Additional fee applies**. 5. **InPerson** means the Ezsignsigner will only be able to sign \&quot;In-Person\&quot; and there won&#39;t be any authentication. No email will be sent for invitation to sign. Make sure you evaluate the risk of signature denial and at minimum, we recommend you use a handwritten signature type. | [optional] 
**s_ezsignsigner_secretanswer** | **str** | The predefined answer to the secret question the Ezsignsigner will need to provide to successfully authenticate. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


