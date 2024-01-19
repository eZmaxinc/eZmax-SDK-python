# EzsigndiscussionRequestCompound

A Ezsigndiscussion Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndiscussion_id** | **int** | The unique ID of the Ezsigndiscussion | [optional] 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**i_ezsigndiscussion_pagenumber** | **int** | The page number in the Ezsigndocument for the Ezsigndiscussion | 
**i_ezsigndiscussion_x** | **int** | The x of the Ezsigndiscussion | 
**i_ezsigndiscussion_y** | **int** | The y of the Ezsigndiscussion | 
**obj_discussion** | [**DiscussionRequest**](DiscussionRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndiscussion_request_compound import EzsigndiscussionRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndiscussionRequestCompound from a JSON string
ezsigndiscussion_request_compound_instance = EzsigndiscussionRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsigndiscussionRequestCompound.to_json()

# convert the object into a dict
ezsigndiscussion_request_compound_dict = ezsigndiscussion_request_compound_instance.to_dict()
# create an instance of EzsigndiscussionRequestCompound from a dict
ezsigndiscussion_request_compound_form_dict = ezsigndiscussion_request_compound.from_dict(ezsigndiscussion_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


