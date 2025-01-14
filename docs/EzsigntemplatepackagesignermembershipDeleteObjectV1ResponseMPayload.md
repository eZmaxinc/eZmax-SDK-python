# EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload

Payload for DELETE /1/object/ezsigntemplatepackagesignermembership/{pkiEzsigntemplatepackagesignermembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**b_ezsignbulksend_needvalidation** | **bool** | Whether the Ezsigntemplatepackage was automatically modified and needs a manual validation | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload import EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload from a JSON string
ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload_instance = EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload_dict = ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload from a dict
ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload_from_dict = EzsigntemplatepackagesignermembershipDeleteObjectV1ResponseMPayload.from_dict(ezsigntemplatepackagesignermembership_delete_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


