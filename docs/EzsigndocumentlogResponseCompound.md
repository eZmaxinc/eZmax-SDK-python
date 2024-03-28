# EzsigndocumentlogResponseCompound

An Ezsigndocumentlog Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_ezsignsigner_id** | **int** | The unique ID of the Ezsignsigner | [optional] 
**dt_ezsigndocumentlog_datetime** | **str** | The date and time at which the event was logged | 
**e_ezsigndocumentlog_type** | [**FieldEEzsigndocumentlogType**](FieldEEzsigndocumentlogType.md) |  | 
**s_ezsigndocumentlog_detail** | **str** | The detail of the Ezsigndocumentlog | 
**s_ezsigndocumentlog_lastname** | **str** | The last name of the User or Ezsignsigner | 
**s_ezsigndocumentlog_firstname** | **str** | The first name of the User or Ezsignsigner | 
**s_ezsigndocumentlog_ip** | **str** | Represent an IP address. | 

## Example

```python
from eZmaxApi.models.ezsigndocumentlog_response_compound import EzsigndocumentlogResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentlogResponseCompound from a JSON string
ezsigndocumentlog_response_compound_instance = EzsigndocumentlogResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentlogResponseCompound.to_json())

# convert the object into a dict
ezsigndocumentlog_response_compound_dict = ezsigndocumentlog_response_compound_instance.to_dict()
# create an instance of EzsigndocumentlogResponseCompound from a dict
ezsigndocumentlog_response_compound_form_dict = ezsigndocumentlog_response_compound.from_dict(ezsigndocumentlog_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


