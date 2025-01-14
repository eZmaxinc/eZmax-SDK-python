# ColleagueRequestCompoundV2

A Colleague Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_colleague_id** | **int** | The unique ID of the Colleague | [optional] 
**fki_user_id** | **int** | The unique ID of the User | 
**fki_user_id_colleague** | **int** | The unique ID of the User | 
**b_colleague_ezsignemail** | **bool** | Whether the email can be used by the cloning user in Ezsign | 
**b_colleague_financial** | **bool** | Whether the cloning user has access to the financial | 
**b_colleague_usecloneemail** | **bool** | Whether the cloning user has access to the cloned user email to send communications | 
**b_colleague_attachment** | **bool** | Whether the cloning user has access to the attachment | 
**b_colleague_canafe** | **bool** | Whether the cloning user has access to canafe | 
**b_colleague_permission** | **bool** | Whether the cloning user copies the permission of the cloned user | 
**b_colleague_realestatecompleted** | **bool** | Whether if the cloning user has access to the completed folders in real estate | 
**dt_colleague_from** | **str** | The from of the Colleague | [optional] 
**dt_colleague_to** | **str** | The to of the Colleague | [optional] 
**e_colleague_ezsign** | [**FieldEColleagueEzsign**](FieldEColleagueEzsign.md) |  | 
**e_colleague_realestateinprogress** | [**FieldEColleagueRealestateinprogess**](FieldEColleagueRealestateinprogess.md) |  | 

## Example

```python
from eZmaxApi.models.colleague_request_compound_v2 import ColleagueRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of ColleagueRequestCompoundV2 from a JSON string
colleague_request_compound_v2_instance = ColleagueRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(ColleagueRequestCompoundV2.to_json())

# convert the object into a dict
colleague_request_compound_v2_dict = colleague_request_compound_v2_instance.to_dict()
# create an instance of ColleagueRequestCompoundV2 from a dict
colleague_request_compound_v2_from_dict = ColleagueRequestCompoundV2.from_dict(colleague_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


