# ColleagueResponseV2

A Colleague Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_colleague_id** | **int** | The unique ID of the Colleague | 
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
**obj_user_name** | [**CustomUserNameResponse**](CustomUserNameResponse.md) |  | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.colleague_response_v2 import ColleagueResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of ColleagueResponseV2 from a JSON string
colleague_response_v2_instance = ColleagueResponseV2.from_json(json)
# print the JSON string representation of the object
print(ColleagueResponseV2.to_json())

# convert the object into a dict
colleague_response_v2_dict = colleague_response_v2_instance.to_dict()
# create an instance of ColleagueResponseV2 from a dict
colleague_response_v2_from_dict = ColleagueResponseV2.from_dict(colleague_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


