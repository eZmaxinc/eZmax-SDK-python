# SystemconfigurationResponseCompound

A Systemconfiguration Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_systemconfiguration_id** | **int** | The unique ID of the Systemconfiguration | 
**fki_systemconfigurationtype_id** | **int** | The unique ID of the Systemconfigurationtype | 
**s_systemconfigurationtype_description_x** | **str** | The description of the Systemconfigurationtype in the language of the requester | 
**e_systemconfiguration_newexternaluseraction** | [**FieldESystemconfigurationNewexternaluseraction**](FieldESystemconfigurationNewexternaluseraction.md) |  | 
**e_systemconfiguration_language1** | [**FieldESystemconfigurationLanguage1**](FieldESystemconfigurationLanguage1.md) |  | 
**e_systemconfiguration_language2** | [**FieldESystemconfigurationLanguage2**](FieldESystemconfigurationLanguage2.md) |  | 
**e_systemconfiguration_ezsign** | [**FieldESystemconfigurationEzsign**](FieldESystemconfigurationEzsign.md) |  | [optional] 
**e_systemconfiguration_ezsignofficeplan** | [**FieldESystemconfigurationEzsignofficeplan**](FieldESystemconfigurationEzsignofficeplan.md) |  | [optional] 
**b_systemconfiguration_ezsignpaidbyoffice** | **bool** | Whether if Ezsign is paid by the company or not | [optional] 
**b_systemconfiguration_ezsignpersonnal** | **bool** | Whether if we allow the creation of personal files in eZsign | 
**b_systemconfiguration_isdisposalactive** | **bool** | Whether is Disposal processus is active or not | [optional] 
**b_systemconfiguration_sspr** | **bool** | Whether if we allow SSPR | 
**dt_systemconfiguration_readonlyexpirationstart** | **str** | The start date where the system will be in read only | [optional] 
**dt_systemconfiguration_readonlyexpirationend** | **str** | The end date where the system will be in read only | [optional] 

## Example

```python
from eZmaxApi.models.systemconfiguration_response_compound import SystemconfigurationResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationResponseCompound from a JSON string
systemconfiguration_response_compound_instance = SystemconfigurationResponseCompound.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationResponseCompound.to_json())

# convert the object into a dict
systemconfiguration_response_compound_dict = systemconfiguration_response_compound_instance.to_dict()
# create an instance of SystemconfigurationResponseCompound from a dict
systemconfiguration_response_compound_form_dict = systemconfiguration_response_compound.from_dict(systemconfiguration_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


