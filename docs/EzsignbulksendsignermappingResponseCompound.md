# EzsignbulksendsignermappingResponseCompound

A Ezsignbulksendsignermapping Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksendsignermapping_id** | **int** | The unique ID of the Ezsignbulksendsignermapping | 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**s_ezsignbulksendsignermapping_description** | **str** | The description of the Ezsignbulksendsignermapping | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_response_compound import EzsignbulksendsignermappingResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingResponseCompound from a JSON string
ezsignbulksendsignermapping_response_compound_instance = EzsignbulksendsignermappingResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendsignermappingResponseCompound.to_json()

# convert the object into a dict
ezsignbulksendsignermapping_response_compound_dict = ezsignbulksendsignermapping_response_compound_instance.to_dict()
# create an instance of EzsignbulksendsignermappingResponseCompound from a dict
ezsignbulksendsignermapping_response_compound_form_dict = ezsignbulksendsignermapping_response_compound.from_dict(ezsignbulksendsignermapping_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


