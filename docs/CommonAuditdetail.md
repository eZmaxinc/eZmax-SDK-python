# CommonAuditdetail

Gives informations about the user that created the object or the last user to have modified it.  If the object was never modified after creation, both Created and Modified informations will be the same. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id** | **int** | The unique ID of the User | 
**fki_apikey_id** | **int** | The unique ID of the Apikey | [optional] 
**s_user_loginname** | **str** | The login name of the User. | 
**s_user_lastname** | **str** | The last name of the user | 
**s_user_firstname** | **str** | The first name of the user | 
**s_apikey_description_x** | **str** | The description of the Apikey in the language of the requester | [optional] 
**dt_auditdetail_date** | **str** | Represent a Date Time. The timezone is the one configured in the User&#39;s profile. | 

## Example

```python
from eZmaxApi.models.common_auditdetail import CommonAuditdetail

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAuditdetail from a JSON string
common_auditdetail_instance = CommonAuditdetail.from_json(json)
# print the JSON string representation of the object
print(CommonAuditdetail.to_json())

# convert the object into a dict
common_auditdetail_dict = common_auditdetail_instance.to_dict()
# create an instance of CommonAuditdetail from a dict
common_auditdetail_form_dict = common_auditdetail.from_dict(common_auditdetail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


