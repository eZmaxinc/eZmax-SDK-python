# CommonAudit

Gives informations about the user that created the object and the last user to have modified it.  If the object was never modified after creation, objAuditdetailModified won't be returned. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_auditdetail_created** | [**CommonAuditdetail**](CommonAuditdetail.md) |  | 
**obj_auditdetail_modified** | [**CommonAuditdetail**](CommonAuditdetail.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.common_audit import CommonAudit

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAudit from a JSON string
common_audit_instance = CommonAudit.from_json(json)
# print the JSON string representation of the object
print(CommonAudit.to_json())

# convert the object into a dict
common_audit_dict = common_audit_instance.to_dict()
# create an instance of CommonAudit from a dict
common_audit_from_dict = CommonAudit.from_dict(common_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


