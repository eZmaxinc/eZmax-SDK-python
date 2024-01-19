# EzsigndiscussionRequest

An Ezsigndiscussion Object

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
from eZmaxApi.models.ezsigndiscussion_request import EzsigndiscussionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndiscussionRequest from a JSON string
ezsigndiscussion_request_instance = EzsigndiscussionRequest.from_json(json)
# print the JSON string representation of the object
print EzsigndiscussionRequest.to_json()

# convert the object into a dict
ezsigndiscussion_request_dict = ezsigndiscussion_request_instance.to_dict()
# create an instance of EzsigndiscussionRequest from a dict
ezsigndiscussion_request_form_dict = ezsigndiscussion_request.from_dict(ezsigndiscussion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


