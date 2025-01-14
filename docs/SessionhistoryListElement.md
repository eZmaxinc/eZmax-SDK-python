# SessionhistoryListElement

A Sessionhistory List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_sessionhistory_id** | **int** | The unique ID of the Sessionhistory | 
**fki_computer_id** | **int** | The unique ID of the Computer | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**dt_sessionhistory_firsthit** | **str** | The first hit of the Sessionhistory | 
**dt_sessionhistory_lasthit** | **str** | The last hit of the Sessionhistory | 
**e_sessionhistory_endby** | [**FieldESessionhistoryEndby**](FieldESessionhistoryEndby.md) |  | 
**s_computer_description** | **str** | The description of the Computer | [optional] 
**s_sessionhistory_duration** | **str** | The duration of the session | 
**s_sessionhistory_ip** | **str** | Represent an IP address. | 
**s_user_loginname** | **str** | The login name of the User. | [optional] 

## Example

```python
from eZmaxApi.models.sessionhistory_list_element import SessionhistoryListElement

# TODO update the JSON string below
json = "{}"
# create an instance of SessionhistoryListElement from a JSON string
sessionhistory_list_element_instance = SessionhistoryListElement.from_json(json)
# print the JSON string representation of the object
print(SessionhistoryListElement.to_json())

# convert the object into a dict
sessionhistory_list_element_dict = sessionhistory_list_element_instance.to_dict()
# create an instance of SessionhistoryListElement from a dict
sessionhistory_list_element_from_dict = SessionhistoryListElement.from_dict(sessionhistory_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


