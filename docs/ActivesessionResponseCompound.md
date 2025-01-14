# ActivesessionResponseCompound

Payload for GET /1/object/activesession/getCurrent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_activesession_usertype** | [**FieldEActivesessionUsertype**](FieldEActivesessionUsertype.md) |  | 
**e_activesession_origin** | [**FieldEActivesessionOrigin**](FieldEActivesessionOrigin.md) |  | 
**e_activesession_weekdaystart** | [**FieldEActivesessionWeekdaystart**](FieldEActivesessionWeekdaystart.md) |  | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | 
**b_activesession_debug** | **bool** | Whether the active session is in debug or not | 
**b_activesession_issuperadmin** | **bool** | Whether the active session is superadmin or not | 
**b_activesession_attachment** | **bool** | Can access attachment when we clone a user | [optional] 
**b_activesession_canafe** | **bool** | Can access canafe when we clone a user | [optional] 
**b_activesession_financial** | **bool** | Can access financial element when we clone a user | [optional] 
**b_activesession_realestatecompleted** | **bool** | Can access closed realestate folders when we clone a user | [optional] 
**e_activesession_ezsign** | [**FieldEActivesessionEzsign**](FieldEActivesessionEzsign.md) |  | [optional] 
**e_activesession_ezsignaccess** | [**FieldEActivesessionEzsignaccess**](FieldEActivesessionEzsignaccess.md) |  | 
**e_activesession_ezsignprepaid** | [**FieldEActivesessionEzsignprepaid**](FieldEActivesessionEzsignprepaid.md) |  | [optional] 
**e_activesession_realestateinprogress** | [**FieldEActivesessionRealestateinprogress**](FieldEActivesessionRealestateinprogress.md) |  | [optional] 
**pks_customer_code** | **str** | The customer code assigned to your account | 
**fki_systemconfigurationtype_id** | **int** | The unique ID of the Systemconfigurationtype | 
**fki_signature_id** | **int** | The unique ID of the Signature | [optional] 
**fki_ezsignuser_id** | **int** | The unique ID of the Ezsignuser | [optional] 
**b_systemconfiguration_ezsignpaidbyoffice** | **bool** | Whether if Ezsign is paid by the company or not | [optional] 
**e_systemconfiguration_ezsignofficeplan** | [**FieldESystemconfigurationEzsignofficeplan**](FieldESystemconfigurationEzsignofficeplan.md) |  | [optional] 
**e_user_ezsignaccess** | [**FieldEUserEzsignaccess**](FieldEUserEzsignaccess.md) |  | 
**e_user_ezsignprepaid** | [**FieldEUserEzsignprepaid**](FieldEUserEzsignprepaid.md) |  | [optional] 
**b_user_ezsigntrial** | **bool** | Whether the User&#39;s eZsign subscription is a trial | [optional] 
**dt_user_ezsignprepaidexpiration** | **str** | The eZsign prepaid expiration date | [optional] 
**a_pki_permission_id** | **List[int]** | An array of permissions granted to the user or api key | 
**obj_user_real** | [**ActivesessionResponseCompoundUser**](ActivesessionResponseCompoundUser.md) |  | 
**obj_user_cloned** | [**ActivesessionResponseCompoundUser**](ActivesessionResponseCompoundUser.md) |  | [optional] 
**obj_apikey** | [**ActivesessionResponseCompoundApikey**](ActivesessionResponseCompoundApikey.md) |  | [optional] 
**a_e_module_internalname** | **List[str]** | An Array of Registered modules.  These are the modules that are Licensed to be used by the User or the API Key. | 

## Example

```python
from eZmaxApi.models.activesession_response_compound import ActivesessionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionResponseCompound from a JSON string
activesession_response_compound_instance = ActivesessionResponseCompound.from_json(json)
# print the JSON string representation of the object
print(ActivesessionResponseCompound.to_json())

# convert the object into a dict
activesession_response_compound_dict = activesession_response_compound_instance.to_dict()
# create an instance of ActivesessionResponseCompound from a dict
activesession_response_compound_from_dict = ActivesessionResponseCompound.from_dict(activesession_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


