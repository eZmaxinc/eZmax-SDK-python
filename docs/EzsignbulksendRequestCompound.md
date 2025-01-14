# EzsignbulksendRequestCompound

A Ezsignbulksend Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_ezsignbulksend_description** | **str** | The description of the Ezsignbulksend | 
**t_ezsignbulksend_note** | **str** | Note about the Ezsignbulksend | 
**b_ezsignbulksend_needvalidation** | **bool** | Whether the Ezsigntemplatepackage was automatically modified and needs a manual validation | 
**b_ezsignbulksend_isactive** | **bool** | Whether the Ezsignbulksend is active or not | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_request_compound import EzsignbulksendRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendRequestCompound from a JSON string
ezsignbulksend_request_compound_instance = EzsignbulksendRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendRequestCompound.to_json())

# convert the object into a dict
ezsignbulksend_request_compound_dict = ezsignbulksend_request_compound_instance.to_dict()
# create an instance of EzsignbulksendRequestCompound from a dict
ezsignbulksend_request_compound_from_dict = EzsignbulksendRequestCompound.from_dict(ezsignbulksend_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


