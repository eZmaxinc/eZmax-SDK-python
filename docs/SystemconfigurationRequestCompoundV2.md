# SystemconfigurationRequestCompoundV2

A Systemconfiguration Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_systemconfiguration_id** | **int** | The unique ID of the Systemconfiguration | [optional] 
**fki_branding_id** | **int** | The unique ID of the Branding | [optional] 
**e_systemconfiguration_newexternaluseraction** | [**FieldESystemconfigurationNewexternaluseraction**](FieldESystemconfigurationNewexternaluseraction.md) |  | 
**e_systemconfiguration_language1** | [**FieldESystemconfigurationLanguage1**](FieldESystemconfigurationLanguage1.md) |  | 
**e_systemconfiguration_language2** | [**FieldESystemconfigurationLanguage2**](FieldESystemconfigurationLanguage2.md) |  | 
**e_systemconfiguration_ezsignofficeplan** | [**FieldESystemconfigurationEzsignofficeplan**](FieldESystemconfigurationEzsignofficeplan.md) |  | [optional] 
**b_systemconfiguration_ezsignpaidbyoffice** | **bool** | Whether if Ezsign is paid by the company or not | [optional] 
**b_systemconfiguration_ezsignpersonnal** | **bool** | Whether if we allow the creation of personal files in eZsign | 
**b_systemconfiguration_sspr** | **bool** | Whether if we allow SSPR | 
**dt_systemconfiguration_readonlyexpirationstart** | **str** | The start date where the system will be in read only | [optional] 
**dt_systemconfiguration_readonlyexpirationend** | **str** | The end date where the system will be in read only | [optional] 
**i_systemconfiguration_ezsignreminderhoursend** | **int** | The hour we will send the eZsign reminders | 

## Example

```python
from eZmaxApi.models.systemconfiguration_request_compound_v2 import SystemconfigurationRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationRequestCompoundV2 from a JSON string
systemconfiguration_request_compound_v2_instance = SystemconfigurationRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationRequestCompoundV2.to_json())

# convert the object into a dict
systemconfiguration_request_compound_v2_dict = systemconfiguration_request_compound_v2_instance.to_dict()
# create an instance of SystemconfigurationRequestCompoundV2 from a dict
systemconfiguration_request_compound_v2_from_dict = SystemconfigurationRequestCompoundV2.from_dict(systemconfiguration_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


