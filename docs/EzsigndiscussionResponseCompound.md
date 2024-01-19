# EzsigndiscussionResponseCompound

A Ezsigndiscussion Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndiscussion_id** | **int** | The unique ID of the Ezsigndiscussion | 
**fki_ezsignpage_id** | **int** | The unique ID of the Ezsignpage | 
**fki_discussion_id** | **int** | The unique ID of the Discussion | 
**i_ezsigndiscussion_x** | **int** | The x of the Ezsigndiscussion | 
**i_ezsigndiscussion_y** | **int** | The y of the Ezsigndiscussion | 
**i_ezsigndiscussion_pagenumber** | **int** | The page number in the Ezsigndocument for the Ezsigndiscussion | 
**obj_discussion** | [**DiscussionResponseCompound**](DiscussionResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndiscussion_response_compound import EzsigndiscussionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndiscussionResponseCompound from a JSON string
ezsigndiscussion_response_compound_instance = EzsigndiscussionResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsigndiscussionResponseCompound.to_json()

# convert the object into a dict
ezsigndiscussion_response_compound_dict = ezsigndiscussion_response_compound_instance.to_dict()
# create an instance of EzsigndiscussionResponseCompound from a dict
ezsigndiscussion_response_compound_form_dict = ezsigndiscussion_response_compound.from_dict(ezsigndiscussion_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


