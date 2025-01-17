# ActivesessionResponseCompound

Payload for GET /1/object/activesession/getCurrent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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


